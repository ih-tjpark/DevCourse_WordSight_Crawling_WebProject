from django import template
from new_api.models import Keyword
register = template.Library()

@register.simple_tag
def getTrend(value):
    top10key = Keyword.objects.order_by('-count')[:10]
    return top10key
