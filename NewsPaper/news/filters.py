from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post

class PostFilter(FilterSet):
   date_in = DateFilter(
      field_name='date_in',
      widget=DateInput(attrs={'type': 'date'}),
      lookup_expr='date__gte',
      label='Поиск по дате'
   )
   class Meta:
      model = Post
      fields = {
         'title' : ['icontains'],
         'author' : ['exact'],
         'date_in' : ['gt'],
      }
