from unicodedata import name
from django.views.generic.base import View
from pims import admin
from django.urls import path

from . import views

app_name = 'pims'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('allItems/', views.itemListView.as_view(), name='item_list'),
    path('editItem/<int:pk>/', views.editItem.as_view(), name='editItem'),
    path('addItem/', views.additemView.as_view(), name='addItem'),
    path('itemDetails/<int:pk>/', views.itemDetailView.as_view(), name='itemDetails'),
    path('deleteItem/<int:pk>/', views.deleteitem.as_view(), name='deleteItem'),

    path('allContainers/', views.containerListView.as_view(), name='container_list'),
    path('deleteContainer/<int:pk>/', views.deleteContainer.as_view(), name='deleteContainer'),
    path('editContainer/<int:pk>/', views.editContainer.as_view(), name='editContainer'),
    path('addContainer/', views.addcontainerView.as_view(), name='addCont'),
    path('contents/<int:pk>/', views.contentsView.as_view(), name='contents'),

    path('season/<int:pk>/', views.seasonView.as_view(), name='season'),

    path('editIC/<int:pk>/', views.editIC.as_view(), name='editI2C'),
    path('addIC/', views.addICView.as_view(), name='addI2C'),
    path('deleteIC/', views.deleteICView.as_view(), name='deleteI2C'),


    path('test/', views.test.as_view(), name='test'),
    path('styleGuide/', views.styleGuide.as_view(), name='styleGuide'),
    path('sitePlan/', views.sitePlan.as_view(), name='sitePlan'),
]