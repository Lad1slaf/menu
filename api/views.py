import datetime

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Restaurant, Menu, Vote
from .permissions import IsRestaurantAdminOrReadOnly, RestaurantOwnerOrReadOnly, MenuAuthorOrReadOnly, IsEmployee, \
    IsCurrentEmployee, RestaurantOwner
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer, ResultsSerializer, RegisterSerializer, \
    UserSerializer


class RestaurantListAPIView(CreateAPIView):
    """
    Create restaurant
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsRestaurantAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RestaurantDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    View restaurant detail or update restaurant data
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [RestaurantOwnerOrReadOnly]


class MenuListAPIView(ListCreateAPIView):
    """
    Create menu or see list of menus
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [RestaurantOwner]

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user.restaurant_admin)


class MenuDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    View menu detail or update menu data
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [MenuAuthorOrReadOnly]


class VoteListAPIView(CreateAPIView):
    """
    Vote for today menu
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsEmployee]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Change your vote
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsCurrentEmployee]


class ResultListAPIView(ListAPIView):
    """
    Getting current day menu with current vote count
    """
    queryset = Menu.objects.filter(date=datetime.date.today())
    serializer_class = ResultsSerializer
    permission_classes = [IsAuthenticated]


class RegisterApi(generics.GenericAPIView):
    """
    Register API
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
