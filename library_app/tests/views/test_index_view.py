from django.test import TestCase
from django.urls import reverse
from library_app.sample.utilities.factories import create_book, create_author, create_genre


class IndexViewTests(TestCase):
    def test_with_no_objects(self):
        self.__get_response()
        self.__assert_context(0, 0, 0)

    def test_with_objects(self):
        create_book('test', 'test')
        create_author('test', 'test')
        create_genre('test')

        self.__get_response()
        self.__assert_context(1, 1, 1)

    def __get_response(self):
        self.response = self.client.get(reverse('library_app:index'))

    def __assert_context(self, book_count, author_count, genre_count):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context['book_count'], book_count)
        self.assertEqual(self.response.context['author_count'], author_count)
        self.assertEqual(self.response.context['genre_count'], genre_count)
