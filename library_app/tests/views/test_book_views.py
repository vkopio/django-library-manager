from django.urls import reverse
from library_app.tests.extended_test_case import ExtendedTestCase
from library_app.sample.utilities.factories import create_book


class BookViewTests(ExtendedTestCase):
    def test_list_with_no_books(self):
        self.__get_list_response()
        self.assertEqual(self.response.status_code, 200)

    def test_list_with_a_book(self):
        book = create_book('test', 'test')

        self.__get_list_response()
        self.assertIn(book, self.response.context['book_list'])
        self.assertEqual(self.response.status_code, 200)

    def test_detail_with_valid_id(self):
        book = create_book('test', 'test')

        self.__get_detail_response(book.id)
        self.assertEqual(self.response.context['book'], book)
        self.assertEqual(self.response.status_code, 200)

    def test_detail_with_invalid_id(self):
        self.__get_detail_response(1)
        self.assertEqual(self.response.status_code, 404)

    def test_detail_with_logged_in_user(self):
        book = create_book('test', 'test')

        self.login()
        self.__get_detail_response(book.id)
        self.assertEqual(self.response.context['book'], book)
        self.assertEqual(self.response.context['reservation_queue_position'], 0)
        self.assertEqual(self.response.status_code, 200)

    def __get_list_response(self):
        url = reverse('library_app:book_list')
        self.response = self.client.get(url)

    def __get_detail_response(self, book_id):
        url = reverse('library_app:book_detail', args=(book_id,))
        self.response = self.client.get(url)
