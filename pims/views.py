from tempfile import template
from django.db import models
from django.db.models import fields
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.

from .models import item, container, season

# import logging
# logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = 'pims/index.html'
    model = container


class itemListView(generic.ListView):
    template_name = 'pims/item_list.html'
    model = item
    context_object_name = 'item'
    def get_queryset(self):
        return item.objects.all().order_by('name')

class containerListView(generic.ListView):
    template_name = "pims/container_list"
    model = container
    context_object_name = 'container'
    def get_queryset(self):
        return container.objects.all().order_by('row_letter')

class contentsView(generic.ListView):
    template_name = "pims/contents.html"
    model = container
    context_object_name = 'container'
    def get_queryset(self):
        newContainer = container.objects.get(id=self.kwargs['pk'])
        return newContainer.items.all()

class editItem(generic.UpdateView):
    template_name = "pims/editItems.html"
    model = item
    context_object_name = 'item'
    fields = {
        'name',
        'quantity'
    }
    success_url="../allItems/"

class additemView(generic.CreateView):
    model = item
    template_name = 'pims/additems.html'
    fields = {
        'name',
        'quantity'
    }
    success_url="../allItems/"


# * Above views are working as desired

#! TODO HERE
class seasonView(generic.ListView):
    model = season
    template_name = 'pims/season.html'
    context_object_name = 'season'
    def get_queryset(self):
        return season.objects.all()

class seasonDetailView(generic.ListView):
    model = season
    template_name = 'pims/seasonDetail.html'
    context_object_name = 'season'
    def get_queryset(self):
        curSeason = season.objects.get(id=self.kwargs['pk']).id
        return container.objects.filter(season=curSeason)



class deleteitem(generic.DeleteView):
    model = item
    template_name = 'pims/deleteitems.html'
    success_url = "../allItems/"


# class test(generic.ListView):
