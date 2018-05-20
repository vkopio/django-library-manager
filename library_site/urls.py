from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('library/', include('library_app.urls')),
    path('admin/', admin.site.urls),
]
