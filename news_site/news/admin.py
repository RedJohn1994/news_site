from django.contrib import admin
from news.models import NewsModels, CommentsModels


@admin.register(NewsModels)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','date_creation']
# Register your models here.
@admin.register(CommentsModels)

class CommentsAdmin(admin.ModelAdmin):
    pass