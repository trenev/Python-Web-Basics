from django import template

from exam_notes.web.models import Note

register = template.Library()


@register.simple_tag()
def has_note():
    return Note.objects.count() > 0
