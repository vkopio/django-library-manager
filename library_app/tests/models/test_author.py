from django.test import TestCase
from library_app.tests.utils.factories import create_author


class AuthorTestCase(TestCase):
    def setUp(self):
        self.author = create_author('test', 'author')

    def test_str_returns_full_name(self):
        self.assertEqual(self.author.__str__(), "test author")
