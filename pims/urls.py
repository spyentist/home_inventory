from unicodedata import name
from django.views.generic.base import View
from django.urls import path
from . import views


app_name = 'pims'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('allItems/', views.itemList.as_view(), name='item_list'),
    path('editItem/<int:pk>/', views.editItem.as_view(), name='editItem'),
    path('addItem/', views.addItem.as_view(), name='addItem'),
    path('itemDetails/<int:pk>/', views.itemDetail.as_view(), name='itemDetails'),
    path('deleteItem/<int:pk>/', views.deleteitem.as_view(), name='deleteItem'),

    path('allContainers/', views.containerList.as_view(), name='container_list'),
    path('deleteContainer/<int:pk>/', views.deleteContainer.as_view(), name='deleteContainer'),
    path('editContainer/<int:pk>/', views.editContainer.as_view(), name='editContainer'),
    path('addContainer/', views.addContainer.as_view(), name='addCont'),
    path('contents/<int:pk>/', views.contents.as_view(), name='contents'),

    path('season/<int:pk>/', views.season.as_view(), name='season'),

    path('editIC/<int:pk>/', views.editIC.as_view(), name='editI2C'),
    path('addIC/', views.addIC.as_view(), name='addI2C'),
    path('deleteIC/', views.deleteIC.as_view(), name='deleteI2C'),


    # Extra pages, to be removed in future
    path('test/', views.test.as_view(), name='test'),
    path('styleGuide/', views.styleGuide.as_view(), name='styleGuide'),
    path('sitePlan/', views.sitePlan.as_view(), name='sitePlan'),
]