from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('howtoplay/', views.howtoplay, name='howtoplay/'),
    path('rules', views.rules, name='rules'),
    path('success', views.success, name='success'),
    path('support/', views.support, name='support/'),
    path('home', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]