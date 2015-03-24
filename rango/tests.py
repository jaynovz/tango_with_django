"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from rango.models import Category
from rango.views import get_category_list


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

from views import decode_url, encode_url
class TestDecodeUrl(TestCase):
    def test_valid_url_decode(self):
        test_phrase = "I_Am_Cat"
        self.assertEqual(decode_url(test_phrase), "I Am Cat")
        
class TestEncodeUrl(TestCase):
    def test_valid_url_encode(self):
        test_phrase = "I Am Cat"
        self.assertEqual(encode_url(test_phrase), "I_Am_Cat")


class TestGetCategories(TestCase):
    def setUp(self):
        Category.objects.create(name='Leia shoes')
        Category.objects.create(name='Fuzz pants')
        Category.objects.create(name='Bbone')

    def test_get_categories_three_categories(self):
        cat_list = get_category_list()
        self.assertEqual(len(cat_list), 3)
        self.assertEqual(cat_list[0].name, 'Leia shoes')
        self.assertEqual(cat_list[1].name, 'Fuzz pants')
        self.assertEqual(cat_list[2].name, 'Bbone')
