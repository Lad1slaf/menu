from django.urls import path
from .views import RestaurantListAPIView, RestaurantDetailAPIView, MenuDetailAPIView, MenuListAPIView, \
    VoteDetailAPIView, VoteListAPIView, ResultListAPIView, RegisterApi

urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('restaurant/create', RestaurantListAPIView.as_view(), name='create_restaurant'),
    path('restaurant/<int:pk>', RestaurantDetailAPIView.as_view(), name='restaurant_detail'),
    path('restaurant/add_menu/', MenuListAPIView.as_view(), name='add_menu'),
    path('restaurant/menu/<int:pk>', MenuDetailAPIView.as_view(), name='menu_detail'),
    path('employee/vote/', VoteListAPIView.as_view(), name='add_vote'),
    path('employee/change_vote/<int:pk>', VoteDetailAPIView.as_view(), name='vote_detail'),
    path('results/', ResultListAPIView.as_view(), name='results'),
]
