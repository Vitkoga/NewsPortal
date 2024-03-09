from django import template
import re

register = template.Library()

BED_WORDS = ['дурак', 'чурка', 'чурбан', 'телка']

# @register.filter()
# def censor(value):
#     words = value.split()  # Проводим разделение фразы на отдельные слова.
#     for word in words:
#         found = word in BED_WORDS  # Ищем полное совпадение слова среди полученных.
#         if found:
#             str_n = [word]
#             words += re.sub(r'str_n', '*')
#             value = " ".join(words)
#
#     return value

# @register.filter()
# def censor(value):
#     # ls = (value.lower()).split()
#     value = value.lower()
#     print(ls)
#     count = len(BED_WORDS)
#     for i in count:
#         value.replace(BED_WORDS[i], )
#     string = ' '.join(ls)
#     # words = string.split(' ')
#     # for word in BED_WORDS:
#     #     string.replace(word, str('*'*len(word)))
#     # print(string.capitalize())
#     print(string.capitalize())
#
#     return string.capitalize()

@register.filter()
def censor(value):
    for word in value.split():
        if word in BED_WORDS:
            value = value.replace(word, str('*'* len(word)))
    return value.capitalize()
