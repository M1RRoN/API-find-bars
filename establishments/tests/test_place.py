from django.test import TestCase

from categories.models import Category
from establishments.models import Place


class PlaceTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.place = Place.objects.create(
            name='Test Place',
            address='123 Main St',
            category=self.category,
            latitude=37.7749,
            longitude=-122.4194
        )

    def test_place_creation(self):
        self.assertTrue(isinstance(self.place, Place))
        self.assertEqual(self.place.__str__(), self.place.name)

    def test_place_category(self):
        self.assertEqual(self.place.category, self.category)