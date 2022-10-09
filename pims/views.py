from tempfile import template
from django.views import generic
from django.db.models import Sum as sum

from pims.forms import containerForm

# Create your views here.

from .models import item, container, item_container, season

from django.db import connection

# http://localhost:8000/pims/
class Index(generic.TemplateView):
    template_name = 'pims/index.html'
    model = container

#! ITEM VIEWS
# http://localhost:8000/pims/allItems/
class itemList(generic.ListView):
    template_name = 'pims/item_list.html'
    model = item
    context_object_name = 'item'
    def get_queryset(self):
        return item.objects.all().order_by('name')

# http://localhost:8000/pims/itemDetails/#/
class itemDetail(generic.ListView):
    template_name = "pims/itemDetails.html"
    model = item
    context_object_name = 'results'
    def get_queryset(self):
        results = item.objects.get(id=self.kwargs['pk']).item_container_set.all()
        total = item.objects.get(id=self.kwargs['pk']).item_container_set.all().aggregate(total=sum('quantity'))
        return  {'results': results, 'total':total}

#http://localhost:8000/pims/editItem/#/
class editItem(generic.UpdateView):
    template_name = "pims/edit.html"
    model = item
    context_object_name = 'item'
    fields = {
        'name'
    }
    success_url="../../allItems/"

# http://localhost:8000/pims/addItem/
class addItem(generic.CreateView):
    model = item
    template_name = 'pims/add.html'
    fields = {
        'name'
    }
    success_url="../allItems/"
    def get_context_data(self, **kwargs):
        print(self)
        context = super().get_context_data(**kwargs)
        context["title"] = "Add an Item"
        print(context)
        return context

# http://localhost:8000/pims/deleteItem/12/
class deleteitem(generic.DeleteView):
    model = item
    template_name = 'pims/deleteitems.html'
    success_url = "../../allItems/"



#! CONTAINER VIEWS
# http://localhost:8000/pims/allcontainers/
class containerList(generic.ListView):
    template_name = "pims/container_list"
    model = container
    context_object_name = 'container'
    def get_queryset(self):
        return container.objects.all().order_by('location')

# http://localhost:8000/pims/contents/#/
class contents(generic.ListView):
    template_name = "pims/contents.html"
    model = container
    context_object_name = 'container'
    def get_queryset(self):
        newContainer = container.objects.get(id=self.kwargs['pk'])
        return newContainer.item_container_set.all()

# 
class editContainer(generic.UpdateView):
    template_name = "pims/edit.html"
    model = container
    context_object_name = 'item'
    form_class = containerForm
    success_url="../../allContainers/"

#
class addContainer(generic.CreateView):
    model = container
    template_name = 'pims/add.html'
    success_url="../allContainers/"
    form_class = containerForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add a Container"
        return context

#
class deleteContainer(generic.DeleteView):
    model = container
    template_name = 'pims/deleteitems.html'
    success_url = "../../allContainers/"




# * Above views are working as desired









class editIC(generic.UpdateView):
    template_name = "pims/edit.html"
    model = item_container
    context_object_name = 'item'
    fields = {
        'item',
        'quantity',
        'container'
    }
    success_url="../allItems/"
    #TODO verify this is working correctly



class addIC(generic.CreateView):
    model = item_container
    template_name = 'pims/additemscontainer.html'
    fields = {
        'item',
        'quantity',
        'container'
    }
    success_url="../allItems/"
    #TODO verify this is working correctly


class deleteIC(generic.UpdateView):
    template_name = "pims/edit.html"
    model = item_container
    context_object_name = 'item'
    fields = {
        'item',
        'quantity',
        'container'
    }
    success_url="../allItems/"

class styleGuide(generic.ListView):
    template_name = 'pims/styleGuide.html'
    def get_queryset(self):
        return ''

class sitePlan(generic.ListView):
    template_name = 'pims/sitePlan.html'
    def get_queryset(self):
        return ''

class test(generic.ListView):
    template_name = 'pims/test.html'
    model = item
    context_object_name = 'item'
    def get_queryset(self):
        return item.objects.all().order_by('name')


#TODO
class season(generic.ListView):
    model = season
    template_name = 'pims/season.html'
    context_object_name = 'season'
    def get_queryset(self):
        newSeason = season.objects.get(id=self.kwargs['pk'])
        return newSeason.container.all()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['item'] = item.objects.all()
    #     return context