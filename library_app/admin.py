from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'creation_date', 'modification_date')


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'creation_date', 'modification_date')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_date', 'modification_date')


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'lender', 'due_date', 'creation_date')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('book', 'reserver', 'creation_date')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
admin.site.register(Reservation, ReservationAdmin)
