from django import template

from online_library.library.helpers import get_profile
from online_library.library.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0


@register.simple_tag()
def get_first_name():
    profile = get_profile()
    if profile:
        return profile.first_name
