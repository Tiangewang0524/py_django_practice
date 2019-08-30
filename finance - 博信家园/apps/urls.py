from django.urls import path

from.views import *

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('main', User_main.as_view(), name='user_main'),
    path('activate', Activate.as_view(), name='activate'),
    # path('register', Login.as_view(), name='register'),
]