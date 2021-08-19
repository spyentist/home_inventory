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

class itemListView(generic.ListView):
    template_name = 'pims/item_list.html'
    model = item

    context_object_name = 'item'
    def get_queryset(self):
        return item.objects.all()
# * Above views are working as desired (8/18)

class containerListView(generic.ListView):
    template_name = "pims/container_list"
    model = container

    context_object_name = 'container'
    def get_queryset(self):
        return container.objects.all().order_by('row_letter')

class contentsView(generic.CreateView):
    template_name = "pims/cont_details.html"
    model = item


