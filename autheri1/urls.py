from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('signup-new',views.signup,name="signup-new"),
    path('signout-new',views.signout,name="signout"),
]