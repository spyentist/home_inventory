from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.

from .models import item, container

class IndexView(generic.ListView):
    template_name = 'pims/index.html'
    model = container

    context_object_name = 'containers'
    def get_queryset(self):
        return container.objects.order_by('row_letter')



#TODO Fix the detail view. The items show up sparatically, the container name shows up when the context object name and function are commented out. 

class itemListView(generic.ListView):
    template_name = 'pims/detail.html'
    model = item

    context_object_name = 'item'
    def get_queryset(self):
        return item.objects.all()


class contentsListView(generic.CreateView):
    template_name = "pims/item_list.html"
    model = item
