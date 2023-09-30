from django.urls import path
from .views import sign_in, sign_up, sign_out, profile_detail, change_password, change_avatar

app_name = 'user_auth'

urlpatterns = [
    path('api/sign-in', sign_in, name='sign-in'),
    path('api/sign-up', sign_up, name='sign-up'),
    path('api/sign-out', sign_out, name='sign-out'),
    path('api/profile', profile_detail, name='profile'),
    path('api/profile/password', change_password, name='change-password'),
    path('api/profile/avatar', change_avatar, name='change-avatar'),
]
