import datetime

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Restaurant, Menu, Vote
from .permissions import IsRestaurantAdminOrReadOnly, RestaurantOwnerOrReadOnly, MenuAuthorOrReadOnly, IsEmployee, \
    IsCurrentEmployee
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer, ResultsSerializer, RegisterSerializer, \
    UserSerializer


class RestaurantListAPIView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsRestaurantAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RestaurantDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [RestaurantOwnerOrReadOnly]


class MenuListAPIView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsRestaurantAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user.restaurant_admin)


class MenuDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [MenuAuthorOrReadOnly]


class VoteListAPIView(ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsEmployee]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsCurrentEmployee]


class ResultListAPIView(ListAPIView):
    queryset = sorted(Menu.objects.filter(date=datetime.date.today()), key=lambda t: t.vote_count)
    serializer_class = ResultsSerializer
    permission_classes = [IsAuthenticated]


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
