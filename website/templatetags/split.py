from django.template import Library


register = Library()

def split(value, arg):
    return value.split(arg)

def get(value, arg):
    return value[arg]

register.filter(split)
register.filter(get)