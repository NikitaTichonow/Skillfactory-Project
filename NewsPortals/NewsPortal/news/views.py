from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NewsForm, ArticleForm
from .models import Post, Category
from .filters import PostFilter

# ====== Стартовая страница ============================================================================================
def Start_Padge(request):
    news = Post.objects.filter(type='NW').order_by('-dateCreation')
    return render(request, 'flatpages/news.html', {'news': news})

def start(request):
    return render(request, 'flatpages/start.html', {'news': Post.objects.all()},)


# ====== Новости =======================================================================================================
class NewsList(ListView):
    paginate_by = 10 # вот так мы можем указать количество записей на странице
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        # context['value1'] = None   # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['countposts'] = 'posts|length'
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(categoryType='NW')
        return queryset.order_by('-dateCreation')


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'


class NewsCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    raise_exception = True
    form_class = NewsForm
    model = Post
    template_name = 'news/news_create.html'

    def form_valid(self, form):
        form.instance.categoryType = 'NW'
        return super().form_valid(form)


class NewsEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
        permission_required = ('news.add_post',)
        raise_exception = True
        form_class = NewsForm
        model = Post
        template_name = 'news/news_edit.html'


class NewsDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.add_post',)
    raise_exception = True
    model = Post
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')


# ====== Статьи ========================================================================================================
class ArticleList(ListView):
    paginate_by = 10 # вот так мы можем указать количество записей на странице
    model = Post
    template_name = 'news/article_list.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        # context['value1'] = None   # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['countposts'] = 'posts|length'
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(categoryType='AR')
        return queryset.order_by('-dateCreation')


class ArticleDetail(DetailView):
    model = Post
    template_name = 'news/article_detail.html'
    context_object_name = 'post'


class ArticleCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    raise_exception = True
    model = Post
    form_class = ArticleForm
    template_name = 'news/article_create.html'


class ArticleEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.add_post',)
    raise_exception = True
    model = Post
    form_class = ArticleForm
    template_name = 'news/article_edit.html'


class ArticleDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.add_post',)
    raise_exception = True
    model = Post
    template_name = 'news/article_delete.html'
    success_url = reverse_lazy('article_list')



# ====== Поиск =========================================================================================================
class Search(ListView):
    model = Post
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    filterset_class = PostFilter
    paginate_by = 7

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        context['categories'] = Category.objects.all()  # Получение всех категорий
        return context

