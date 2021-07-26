# app/templatetags/timeuntil_fr.py
from django.template import Library
from django.template.defaultfilters import timeuntil_filter
from django.utils import translation

register = Library()

@register.filter
def timeuntil_fr(value, arg=None):
    with translation.override('fr'):
        time_until = timeuntil_filter(value, arg)
    return time_until
