from django.urls import path, re_path

from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, UserDetailAPIView, UserFollowAPIView #, UserFollowingListAPIView

app_name = 'acc'

urlpatterns = [


    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='profile-detail'),
    path('user/<int:pk>/follow', UserFollowAPIView.as_view(), name='follow'),

    # path('user/<int:pk>/following', UserFollowingListAPIView.as_view(), name='following'),
    # path('user/<int:pk>/followers', UserFollowersListAPIView.as_view(), name='followers'),
    # path('users/', UserList.as_view(), name='user-list'),

    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

]
