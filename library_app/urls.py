from django.urls import path
from .apps import LibraryAppConfig
from . import views

app_name = LibraryAppConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/<int:book_id>/reserve', views.reservation_create, name='reservation_create'),
    path('books/<int:book_id>/cancel', views.reservation_delete, name='reservation_delete'),
    path('user/', views.user_detail, name='user_detail'),
]
