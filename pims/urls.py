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
    path('itemDetails/<slug:slug>/', views.itemDetail.as_view(), name='itemDetail'),
    path('deleteItem/<int:pk>/', views.deleteitem.as_view(), name='deleteItem'),

    path('locations/', views.locations.as_view(), name='locations'),
    path('allContainers/', views.containerList.as_view(), name='container_list'),
    path('deleteContainer/<int:pk>/', views.deleteContainer.as_view(), name='deleteContainer'),
    path('editContainer/<int:pk>/', views.editContainer.as_view(), name='editContainer'),
    path('addContainer/', views.addContainer.as_view(), name='addCont'),
    path('contents/<int:pk>/', views.contents.as_view(), name='contents'),

    path('allICs/', views.ICList.as_view(), name='listI2C'),
    path('editIC/<int:pk>/', views.editIC.as_view(), name='editI2C'),
    path('addIC/', views.addIC.as_view(), name='addI2C'),
    path('deleteIC/<int:pk>', views.deleteIC.as_view(), name='deleteI2C'),
    path('ICDetails/<int:pk>', views.ICDetails.as_view(), name='I2CDetails'),




    path('season/<int:pk>/', views.season.as_view(), name='season'),
    path('season/<slug:slug>/', views.season.as_view(), name='season'),
    # Extra pages, to be removed in future
    path('test/', views.test.as_view(), name='test'),
    path('styleGuide/', views.styleGuide.as_view(), name='styleGuide'),
    path('sitePlan/', views.sitePlan.as_view(), name='sitePlan'),
]