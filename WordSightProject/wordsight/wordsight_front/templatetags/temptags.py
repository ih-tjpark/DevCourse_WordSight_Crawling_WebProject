from django import template
from new_api.models import Keyword
register = template.Library()

@register.simple_tag
def getTrend(value):
    top10key = Keyword.objects.order_by('-count')[:10]
    return top10key

@register.filter
def find_tag(Tag, news_id):
    """Returns non zero value if a profile has the option.
    Usage::

        {% if user.profile|does_profile_have_option:option.id %}
        ...
        {% endif %}
    """
    return Tag.options.filter(id=news_id)
