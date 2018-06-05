from django.contrib.auth.models import User


class LibraryUser(User):
    class Meta:
        proxy = True
