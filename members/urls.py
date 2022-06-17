from django.urls import path
from members import views

urlpatterns = [
    path('',views.cover,name='cover'),
    path('login',views.loginview,name='login'),
    path('register',views.registerview,name='register'),
    path('logout',views.logoutview,name='logout'),
    path('home',views.home,name='home'),
    path('join_room',views.join_room,name='join_room'),
]
