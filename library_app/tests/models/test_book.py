from django.test import TestCase
from django.utils import timezone
from library_app.models import Book


class BookTestCase(TestCase):
    def setUp(self):
        self.book = Book(
            name="test-book",
            pub_date=timezone.now().today()
        )

    def test_str_returns_name(self):
        self.assertEqual(self.book.__str__(), "test-book")
