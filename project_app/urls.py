from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('signup-new',views.signup,name="signup-new"),
    path('signout-new',views.signout,name="signout"),
    path('roomallo',views.room_data,name="room_data"),
]
urlpatterns += staticfiles_urlpatterns()