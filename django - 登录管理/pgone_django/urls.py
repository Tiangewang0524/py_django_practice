from django.urls import path

from.views import *

urlpatterns = [
    # path('login/', views.index, name='index'),
    path('login', Login.as_view(), name='login'),
    # path('register', Login.as_view(), name='register'),
    path('write_sql', view_register.as_view(), name='register'),
    path('get_problems', UserMsg.as_view()),
    path('modify_state', Modify_state.as_view()),
]