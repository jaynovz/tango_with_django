"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


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