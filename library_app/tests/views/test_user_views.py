from django.urls import reverse
from library_app.tests.extended_test_case import ExtendedTestCase


class UserViewTests(ExtendedTestCase):
    def test_detail_with_logged_in_user(self):
        self.login()
        self.__get_detail_response()
        self.assertEqual(list(self.response.context['borrowings']), [])
        self.assertEqual(list(self.response.context['reservations']), [])
        self.assertEqual(self.response.status_code, 200)

    def test_detail_without_logging_in(self):
        self.__get_detail_response()
        self.assertEqual(self.response.status_code, 302)

    def __get_detail_response(self):
        url = reverse('library_app:user_detail')
        self.response = self.client.get(url)
