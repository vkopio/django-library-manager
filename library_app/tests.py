from django.test import TestCase
from django.utils import timezone
from .models import *


class BookTestCase(TestCase):
    def setUp(self):
        self.book = Book(
            name="test-book",
            pub_date=timezone.now().today()
        )

    def test_str_returns_name(self):
        self.assertEqual(self.book.__str__(), "test-book")


class AuthorTestCase(TestCase):
    def setUp(self):
        self.author = Author(
            first_name="test",
            last_name='author',
            birth_date=timezone.now().today()
        )

    def test_str_returns_full_name(self):
        self.assertEqual(self.author.__str__(), "test author")


class GenreTestCase(TestCase):
    def setUp(self):
        self.genre = Genre(
            name="test-genre"
        )

    def test_str_returns_name(self):
        self.assertEqual(self.genre.__str__(), "test-genre")
