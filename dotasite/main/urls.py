from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home_page'),
    path('last_pick', views.last_pick, name='last_pick')
]