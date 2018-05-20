from django.test import TestCase
from django.utils import timezone
from library_app.models import Author


class AuthorTestCase(TestCase):
    def setUp(self):
        self.author = Author(
            first_name="test",
            last_name='author',
            birth_date=timezone.now().today()
        )

    def test_str_returns_full_name(self):
        self.assertEqual(self.author.__str__(), "test author")
