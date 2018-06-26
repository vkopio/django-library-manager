from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from contextlib import contextmanager


class ExtendedTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(
            username='test_user',
            password='test',
            email='test@test.test'
        )

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()

    def login(self):
        self.client.force_login(self.user)

    def logout(self):
        self.client.logout()

    def user(self):
        return auth.get_user(self.client)

    @contextmanager
    def assertValidationError(self, field, error_messages=None):
        """
        Assert that a validation error is raised for a given field.
        Optionally assert that an array of error messages is correct.
        """
        try:
            yield
            raise AssertionError("ValidationError not raised")

        except ValidationError as e:
            self.assertTrue(
                field in e.message_dict,
                "ValidationError is raised, but not for field '" + field + "'"
            )

            if error_messages:
                self.assertEqual(
                    error_messages,
                    e.message_dict[field],
                    'Array of error messages did not match the expected'
                )
