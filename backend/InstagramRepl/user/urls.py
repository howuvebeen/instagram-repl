from django.urls import path, include, re_path
from user import views
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('', include('rest_registration.api.urls', 'views.api_root')),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user-detail'),
    path('profiles/', views.ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>', views.ProfileList.as_view(), name='profile-detail'),
]
