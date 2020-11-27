from django import template

from ..scryps import time_convert


register = template.Library()


register.filter('to_time', time_convert)
