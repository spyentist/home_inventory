# from typing import Container
from django.test import TestCase
from .models import *

# Create your tests here.

class testItem(TestCase):
    def setUp(self):
        item.objects.create(name='Chair', quantity=45)
        item.objects.create(name='Desk', quantity=25)
        container.objects.create(location='Office', row_letter='A', column_number=2)

    def test_container_has_items(self):
        cont1 = container.objects.get(location='Office')
        item1 = item.objects.get(name='Chair')
        item2 = item.objects.get(name='Desk')
        cont1.items.add(item1)
        cont1.items.add(item2)
        self.assertEqual(list(item.objects.values('name')), [{'name': 'Chair'}, {'name': 'Desk'}])
        self.assertEqual(list(cont1.items.values('name')), [{'name': 'Chair'}, {'name': 'Desk'}])    
    