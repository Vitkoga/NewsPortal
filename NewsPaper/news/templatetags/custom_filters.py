from django import template

register = template.Library()

BED_WORDS = ['дурак', 'чурка', 'чурбан', 'телка']

@register.filter()
def censor(value):
    for word in value.split():
        if word in BED_WORDS:
            value = value.replace(word, str('*'* len(word)))
    return value.capitalize()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()
