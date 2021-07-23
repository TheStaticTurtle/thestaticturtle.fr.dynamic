from django.template import Library

import re

register = Library()

def search(value, search):
    return re.sub(search, '#f4SgXXmSx@SgXXmSSgXXmSSgXXmS', value)

def replace(value, replace):
    return re.sub('#f4SgXXmSx@SgXXmSSgXXmSSgXXmS', replace, value)

register.filter(search)
register.filter(replace)