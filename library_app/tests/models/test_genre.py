from django.test import TestCase
from library_app.models import Genre


class GenreTestCase(TestCase):
    def setUp(self):
        self.genre = Genre(
            name="test-genre"
        )

    def test_str_returns_name(self):
        self.assertEqual(self.genre.__str__(), "test-genre")
