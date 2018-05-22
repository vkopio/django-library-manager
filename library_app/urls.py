from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book_list_view'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]
