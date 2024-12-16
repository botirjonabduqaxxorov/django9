from django import template
from flowers.models import FlowerType

register = template.Library()

@register.simple_tag
def get_flower_types():
    return FlowerType.objects.all()
