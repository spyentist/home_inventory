# from typing import Container
from django.test import TestCase
from .models import *

# Create your tests here.

class testItemCreation(TestCase):
    def setup(self):
        item.objects.create(name='Test Item')

    def test_item_created(self):
        item.objects.get()


class testItem(TestCase):
    def setUp(self):
        item.objects.create(name='Test Chair')
        item.objects.create(name='Test Desk')
        container.objects.create(location='Garage', row_letter='A', column_number=4)
        container.objects.create(location='Office', row_letter='F', column_number=8)
       

    def test_container_has_items(self):
        item1 = item.objects.get(name='Test Chair').id
        item2 = item.objects.get(name='Test Desk').id
        cont1 = container.objects.get(location='Garage',row_letter='A').id
        cont2 = container.objects.get(location='Office',row_letter='F').id
        m2m1 = item_container.objects.create(quantity='2', item_id=item1, container_id=cont1)
        m2m2 = item_container.objects.create(quantity='5', item_id=item2, container_id=cont1)
        m2m3 = item_container.objects.create(quantity='3', item_id=item1, container_id=cont2)
        self.assertNotEqual(item_container.objects.all(),'')
        # return list(item_container.objects.all())

        
        # self.assertEqual(list(item.objects.values('name')), [{'name': 'Chair'}, {'name': 'Desk'}])
        # self.assertEqual(list(cont1.items.values('name')), [{'name': 'Chair'}, {'name': 'Desk'}])    
    