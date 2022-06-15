from django.views.generic.base import View
from pims import admin
from django.urls import path

from . import views

app_name = 'pims'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('allItems/', views.itemListView.as_view(), name='item_list'),
    path('contents/<int:pk>/', views.contentsView.as_view(), name='contents'),
    path('allContainers/', views.containerListView.as_view(), name='container_list'),
    path('season/<int:pk>/', views.seasonView.as_view(), name='season'),
    path('editItem/<int:pk>/', views.editItem.as_view(), name='editItem'),
    path('editIC/<int:pk>/', views.editIC.as_view(), name='editIC'),
    path('editContainer/<int:pk>/', views.editContainer.as_view(), name='editContainer'),
    path('delete/<int:pk>/', views.deleteitem.as_view(), name='deleteItem'),
    path('delete/<int:pk>/', views.deleteContainer.as_view(), name='deleteContainer'),
    path('test/', views.test.as_view(), name='test'),
    path('addItem/', views.additemView.as_view(), name='addItem'),
    path('addIC/', views.addICView.as_view(), name='I2C'),
    path('addContainer/', views.addcontainerView.as_view(), name='addCont'),
    path('itemDetail/<int:pk>/', views.itemDetailView.as_view(), name='ItemDetail'),
]