from django.urls import path
from . import views
from .views import NewsList, NewsDetail


urlpatterns = [
    path('news/', NewsList.as_view()),  # URL-шаблон для списка новостей
    path('news/<int:pk>', NewsDetail.as_view()),  # URL-шаблон для списка новостей
]

