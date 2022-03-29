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
        print(list(item.objects.values('name')))
        self.assertEqual(list(cont1.items.values('name')), [{'name': 'Chair'}, {'name': 'Desk'}])

class testSeason(TestCase):
    def setUp(self):
        season.objects.create(name='Summer')
        container.objects.create(location='Garage', row_letter='Z', column_number=999)
        item.objects.create(name='Swim Trunks')

    def test_season_has_containers_and_items(self):
        cont1 = container.objects.get(location='Garage')
        item1 = item.objects.get(name='Swim Trunks')
        cont1.items.add(item1)
        season1 = season.objects.get(name='Summer')
        cont1.season.add(season1)
        print(list(cont1.season.values('name')))

        #TODO    Finish the test, print the values of the seasons associated with a container
        #TODO    Get assertions set to make sure the models still work.

        self.assertEqual(list(cont1.season.values('name')),[{'name': 'Summer'}])
