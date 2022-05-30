# Generated by Django 2.2 on 2022-05-28 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='content',
            field=models.CharField(default='', max_length=5000, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='date_creation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='date_edit',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newsmodels',
            name='active',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.ActiveModels'),
        ),
    ]
