"""finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views import View
from django.urls import path, include, re_path
# from django.conf.urls import url
from django.shortcuts import render_to_response


class Rediect_All(View):
    def get(self, request, *args, **kwargs):
        path = kwargs.get('path')
        if not path:
            return render_to_response('../templates/login.html')
        return render_to_response('../templates/' + path + '.html')


urlpatterns = [
    # path('backend/', include('user.urls')),
    # 处理页面跳转
    re_path(r'^bxjy/(?P<path>.*)', Rediect_All.as_view()),    # r'backend/(?P<path>.*)'
    # 处理业务逻辑
    re_path(r'^api/home/', include('apps.urls'))
    # path('admin/', admin.site.urls),s
    # url(r'backend/(?P<path>.*)', include('user.urls')),
]

