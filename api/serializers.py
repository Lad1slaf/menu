import datetime

from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Restaurant, Menu, Vote, CustomUser


class RestaurantSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        try:
            instance, _ = Restaurant.objects.get_or_create(**validated_data)

            return instance
        except:
            raise ValidationError('ERROR: You already created Restaurant')

    class Meta:
        model = Restaurant
        fields = ('pk', 'user', 'name', 'description',)
        read_only_fields = ('user',)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('pk', 'restaurant', 'menu', 'date',)
        read_only_fields = ('date', 'restaurant',)

    def create(self, validated_data):
        menu = Menu(**validated_data)
        today_menus = Menu.objects.filter(
            Q(date=datetime.date.today()) & Q(restaurant=self.context['request'].user.restaurant_admin))
        if today_menus:
            raise ValidationError("Your restaurant are already added menu at that day")
        menu.save()
        return menu


class VoteSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(date=datetime.date.today()))

    class Meta:
        model = Vote
        fields = ('pk', 'user', 'menu', 'date')
        read_only_fields = ('user', 'date')

    def create(self, validated_data):
        vote = Vote(**validated_data)
        voted = Vote.objects.filter(Q(date=datetime.date.today()) & Q(user=self.context['request'].user))
        if voted:
            raise ValidationError("You are already voted today. You can change your vote: change_vote/<int:pk>")
        vote.save()
        return vote


class ResultsSerializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField()

    class Meta:
        model = Menu
        fields = ('pk', 'vote_count', 'restaurant', 'menu', 'date')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'role')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'],
                                              password=validated_data['password'],
                                              role=validated_data['role'])
        return user



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
