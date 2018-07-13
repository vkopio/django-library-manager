from django import template

register = template.Library()


@register.simple_tag
def reservation_queue_position(library_user, book):
    return library_user.reservation_queue_position(book)
