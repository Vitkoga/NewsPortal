from django import template

register = template.Library()

BED_WORDS = ['дурак', 'чурка', 'чурбан', 'телка']

@register.filter()
def censor(value):
    for word in value.split():
        if word in BED_WORDS:
            value = value.replace(word, str('*'* len(word)))
    return value.capitalize()
