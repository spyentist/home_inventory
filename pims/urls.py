from django.views.generic.base import View
from pims import admin
from django.urls import path

from . import views

app_name = 'pims'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('allItems/', views.itemListView.as_view(), name='item_list'),
    path('contents/<int:pk>', views.contentsView.as_view(), name='contents'),
    path('allcontainers/', views.containerListView.as_view(), name='container_list'),
    path('season/', views.seasonView.as_view(), name='season'),
    path('season/<int:pk>', views.seasonDetailView.as_view(), name='seasonDetail'),
    path('edit/<int:pk>', views.editItem.as_view(), name='editItem'),
    path('delete/<int:pk>', views.deleteitem.as_view(), name='deleteItem'),
    # path('test/<int:pk>', views.test.as_view(), name='test'),
    path('addItem/', views.additemView.as_view(), name='addItem')
]