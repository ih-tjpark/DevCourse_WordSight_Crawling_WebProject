from django import template
from new_api.models import Keyword
register = template.Library()

def sort_by(queryset, order):
    return queryset.order_by(order)

@register.filter
def find_tag(Tag, news_id):
    """Returns non zero value if a profile has the option.
    Usage::

        {% if user.profile|does_profile_have_option:option.id %}
        ...
        {% endif %}
    """
    return Tag.options.filter(id=news_id)
