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
        context = super().get_context_data(**kwargs)
        context["title"] = "Add an Item"
        return context

# http://localhost:8000/pims/deleteItem/12/
class deleteitem(generic.DeleteView):
    model = item
    template_name = 'pims/delete.html'
    success_url = "../../allItems/"



#! CONTAINER VIEWS
# http://localhost:8000/pims/allcontainers/
class containerList(generic.ListView):
    template_name = "pims/container_list"
    model = container
    context_object_name = 'container'
    def get_queryset(self):
        return container.objects.all().order_by('location', 'row_letter','column_number')

# http://localhost:8000/pims/contents/#/
class contents(generic.ListView):
    template_name = "pims/contents.html"
    model = container
    context_object_name = 'container'
    def get_queryset(self):
        return container.objects.get(id=self.kwargs['pk'])
        

# http://localhost:8000/pims/editContainer/#/
class editContainer(generic.UpdateView):
    template_name = "pims/edit.html"
    model = container
    context_object_name = 'item'
    form_class = containerForm
    success_url="../../allContainers/"

# http://localhost:8000/pims/addContainer/
class addContainer(generic.CreateView):
    model = container
    template_name = 'pims/add.html'
    success_url="../allContainers/"
    form_class = containerForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add a Container"
        return context

# http://localhost:8000/pims/deleteContainer/#/
class deleteContainer(generic.DeleteView):
    model = container
    template_name = 'pims/delete.html'
    success_url = "../../allContainers/"


# http://127.0.0.1:8000/pims/addIC/
class addIC(generic.CreateView):
    model = item_container
    template_name = 'pims/additemscontainer.html'
    fields = {
        'item',
        'quantity',
        'container'
    }
    success_url="../allICs/"
    #TODO add a search feature to the dropdown fields
    #TODO make batch inserts possible?? i.e. add multiple items to one container at the same time
    #TODO fix css for mobile view

    

# http://127.0.0.1:8000/pims/allICs/
class ICList(generic.ListView):
    model = item_container
    template_name = "pims/ICList.html"
    context_object_name = 'IC'
    def get_queryset(self):
        return item_container.objects.all()
# This one works.... Not sure if it is going to be utilized in the actual program. Good for troubleshooting

# http://127.0.0.1:8000/pims/editIC/1960/
class editIC(generic.UpdateView):
    template_name = "pims/edit.html"
    model = item_container
    context_object_name = 'item'
    fields = {
        'item',
        'quantity',
        'container'
    }
    success_url="../../allICs/"

# http://127.0.0.1:8000/pims/deleteIC/1943
class deleteIC(generic.DeleteView):
    template_name = "pims/delete.html"
    model = item_container
    context_object_name = 'item'
    fields = {
        'item',
        'quantity',
        'container'
    }
    success_url="../allICs/"


class ICDetails(generic.DetailView):
    model = item_container
    template_name = "pims/" 


# * Above views are working as desired

'''
What if a location was able to have multiple containers in it. Need to create new model to represent that. 
'''


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