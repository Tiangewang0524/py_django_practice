from django.urls import path

from.views import *

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('main', User_main.as_view(), name='user_main'),
    path('activate', Activate.as_view(), name='activate'),
    path('buy', Buy.as_view(), name='buy'),
    path('admin', Admin.as_view(), name='admin'),
    path('sell', Sell.as_view(), name='sell'),
    path('match', Match.as_view(), name='match'),
    # path('register', Login.as_view(), name='register'),
]