from library_app.tests.extended_test_case import ExtendedTestCase
from library_app.sample.utilities.factories import create_book, create_borrowing


class GenreTestCase(ExtendedTestCase):
    def setUp(self):
        self.book = create_book("test-book", "")
        self.borrowing = create_borrowing('1970-01-01', book=self.book, borrower=self.user.libraryuser)

    def test_book_borrowings_count_is_updated(self):
        self.assertEqual(self.book.borrowings_count, 1)

    def test_str_returns_desired_format(self):
        self.assertEqual(self.borrowing.__str__(), "test-book, borrower: test_user, due date: 1970-01-01")
