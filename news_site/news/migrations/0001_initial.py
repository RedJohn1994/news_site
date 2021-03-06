# Generated by Django 2.2 on 2022-05-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.CharField(max_length=5000, verbose_name='Содержание')),
                ('date_creation', models.DateField()),
                ('date_edit', models.DateTimeField()),
            ],
        ),
    ]
