from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from news.models import NewsModels, CommentsModels
from news.forms import NewsForms, CommentsForm


def news_about(request):
    return render(request, 'news/news_about.html',{})
    '''Просто выводит основную страницу'''


class NewsAllView(generic.ListView):
    model = NewsModels
    context_object_name = 'news_all'
    '''Выводит модель в шаблон'''


class NewsFormViews(View):
    def get(self, request):
        user_form = NewsForms
        return render(request,'news/add_news.html', context={'user_form':user_form})

    def post(self, request):
        user_form = NewsForms(request.POST)

        if user_form.is_valid():

            NewsModels.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')

        return render(request,'news/add_news.html', context={'user_form':user_form})
    '''Создает 2 поля для заполнения title и content и сохраняет их в модель  NewsModels '''

class NewsCommentView(View):
    def get(self, request):
        comments = CommentsForm
        return render(request,'news/comments.html', context={'comments':comments})

    def post(self, request, *args, **kwargs):
        comments = CommentsForm(request.POST)

        if comments.is_valid():
            CommentsModels.objects.create(**comments.cleaned_data)
            return HttpResponseRedirect('/')

        return render(request,'news/comments.html', context={'comments':comments})

    '''Создает  поле comment и сохраняет их в модель  NewsModels '''




