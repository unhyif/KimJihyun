from django import template
register = template.Library()

@register.simple_tag
def get_verbose_name(object, field): 
  return object._meta.get_field(field).verbose_name.title() # need to check later