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


class itemListView(generic.ListView):
    template_name = 'pims/item_list.html'
    model = item

    context_object_name = 'item'
    def get_queryset(self):
        return item.objects.all()

class containerListView(generic.ListView):
    template_name = "pims/container_list"
    model = container

    context_object_name = 'container'
    def get_queryset(self):
        return container.objects.all().order_by('row_letter')
# * Above views are working as desired


class contentsView(generic.ListView):
    template_name = "pims/contents.html"
    model = item

    def get_queryset(self):
        return item.objects.all()


class testView(generic.DetailView):
    model = item
    template_name = "pims/test.html"

    context_object_name = "item"
    def get_queryset(self):
        return item.objects.all()