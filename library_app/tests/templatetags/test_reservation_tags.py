from library_app.templatetags.reservation_tags import reservation_queue_position
from django.test import TestCase


class LibraryUserMock:
    @staticmethod
    def reservation_queue_position(value):
        return value


class ReservationTagTests(TestCase):
    def setUp(self):
        self.library_user = LibraryUserMock()

    def test_the_tag_calls_library_users_corresponding_method(self):
        self.assertEqual(reservation_queue_position(self.library_user, "test"), "test")
