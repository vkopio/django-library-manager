from library_app.tests.utils.extended_test_case import ExtendedTestCase
from library_app.tests.utils.factories import create_book


class BookTestCase(ExtendedTestCase):
    def setUp(self):
        self.book = create_book("test-book", "")

    def test_str_returns_name(self):
        self.assertEqual(self.book.__str__(), "test-book")

    def test_raises_error_for_invalid_isbn(self):
        self.book.isbn = 'invalid-isbn'

        with self.assertValidationError('isbn', ['invalid-isbn is not a valid ISBN number']):
            self.book.full_clean()

    def test_no_errors_are_raised_for_valid_isbn_10(self):
        self.book.isbn = '951-98548-9-4'
        self.book.full_clean()

    def test_no_errors_are_raised_for_valid_isbn_13(self):
        self.book.isbn = '978-951-98548-9-2'
        self.book.full_clean()
