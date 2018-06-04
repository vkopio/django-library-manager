from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='library', permanent=False), name='home'),
    path('library/', include('library_app.urls')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'home'}, name='logout'),
    path('admin/', admin.site.urls),
]
