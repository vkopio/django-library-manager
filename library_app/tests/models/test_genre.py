from django.test import TestCase
from library_app.sample.utilities.factories import create_genre


class GenreTestCase(TestCase):
    def setUp(self):
        self.genre = create_genre('test-genre')

    def test_str_returns_name(self):
        self.assertEqual(self.genre.__str__(), "test-genre")
