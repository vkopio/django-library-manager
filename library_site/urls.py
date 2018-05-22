from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='library', permanent=False)),
    path('library/', include('library_app.urls')),
    path('admin/', admin.site.urls),
]
