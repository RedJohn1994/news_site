# Generated by Django 2.2 on 2022-05-28 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220528_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(default='', max_length=100, verbose_name='Комментарий')),
            ],
        ),
        migrations.AddField(
            model_name='newsmodels',
            name='comment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.CommentsModels'),
        ),
    ]
