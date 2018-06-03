from django.test import TestCase
from library_app.tests.utils.factories import create_book
from library_app.models import Book


class BookTestCase(TestCase):
    def setUp(self):
        self.book = create_book("test-book", "")

    def test_str_returns_name(self):
        self.assertEqual(self.book.__str__(), "test-book")
