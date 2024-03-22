# Generated by Django 5.0.3 on 2024-03-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Как вас зовут?')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Укажите вашу почту')),
                ('description', models.TextField(null=True, verbose_name='Напишите комментарий')),
            ],
        ),
        migrations.DeleteModel(
            name='ItForum',
        ),
    ]
