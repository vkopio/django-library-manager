from django.apps import AppConfig


class LibraryAppConfig(AppConfig):
    name = 'library_app'


def app_dir(file):
    return LibraryAppConfig.name + '/' + file
