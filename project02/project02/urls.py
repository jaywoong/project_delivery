"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from project02 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    path('index4', views.index4, name='index4'),
    path('index5', views.index5, name='index5'),
    path('index6', views.index6, name='index6'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('quit', views.quit, name='quit'),
    path('quitimpl', views.quitimpl, name='quitimpl'),
    path('loginimpl', views.loginimpl, name='loginimpl'),
    path('signup', views.signup, name='signup'),
    path('useraddimpl', views.useraddimpl, name='useraddimpl'),
    path('quitok', views.quitok, name='quitok'),
    path('registerok', views.registerok, name='registerok'),
    path('profile', views.profile, name='profile'),
    path('ud_profile', views.ud_profile, name='ud_profile'),
    path('userupdateimpl', views.userupdateimpl, name='userupdateimpl'),
    path('analysis', views.analysis, name='analysis'),



]
