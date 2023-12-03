from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter
def date_return(value1):
    td = timedelta(7)
    return (value1 + td)