from django.views.generic.base import View
from pims import admin
from django.urls import path

from . import views

app_name = 'pims'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('allItems/', views.itemListView.as_view(), name='item_list'),
    path('contents/', views.contentsListView.as_view(), name='item'),
    # path('conatiner/<int:pk>/', views.views, name='container'),
    # path('season/', views.views, name='season'),
]