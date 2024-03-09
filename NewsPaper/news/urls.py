from django.urls import path
# Импортируем созданные нами представления
from .views import PostList, PostDetail

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
]