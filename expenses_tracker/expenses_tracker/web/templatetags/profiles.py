from django import template
from expenses_tracker.web.models import Profile, Expense

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0


@register.simple_tag()
def has_expenses():
    return Expense.objects.count() > 0
