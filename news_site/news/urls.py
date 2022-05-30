from django.urls import path
from .import views
from news.views import NewsAllView, NewsFormViews,NewsCommentView
urlpatterns = [
    path('', views.news_about, name = 'name_about'),
    path('newsmodels_list', NewsAllView.as_view(), name = 'newsmodels_list'),
    path('news/add_news', NewsFormViews.as_view()),
    path('news/comments/', NewsCommentView.as_view()),
]