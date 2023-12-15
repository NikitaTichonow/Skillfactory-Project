from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# ====== Стартовая страница ============================================================================================
def Start_Padge(request):
    news = Post.objects.filter(type='NW').order_by('dateCreation')
    return render(request, 'flatpages/start.html', {'news': news})

def start(request):
    return render(request, 'flatpages/start.html')

# ====== Новости =======================================================================================================
class NewsList(ListView):
    paginate_by = 10
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'



