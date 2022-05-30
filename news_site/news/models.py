from django.db import models


class NewsModels(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    content = models.CharField(verbose_name='Содержание', max_length=5000, default='')
    date_creation = models.DateField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    active = models.ForeignKey('ActiveModels', on_delete=models.CASCADE, default=None, null=True)
    comment = models.ForeignKey('CommentsModels', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.comment


class ActiveModels(models.Model):
    text = models.CharField(max_length=20)

    def __str__(self):
        return self.text


class CommentsModels(models.Model):
    comments = models.CharField(verbose_name='Комментарий', max_length=100, default='')

    def __str__(self):
        return self.comments


