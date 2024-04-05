from django.db import models


class BookTag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Напишите тег', default='#')

    def __str__(self):
        return f'#{self.name}'


class Book(models.Model):

    TYPE_BOOKS_CHOICES = (
        ('Художественная литература', 'Художественная литература'),
        ('Детективы', 'Детективы'),
        ('Любовные романы', 'Любовные романы'),
        ('Приключения', 'Приключения'),
        ('Манга', 'Манга')
    )

    title = models.CharField(max_length=50, null=True, verbose_name='Напишите название книги')
    description = models.TextField(null=True, verbose_name='Напишите краткое описание книги')
    price = models.DecimalField(max_digits=1000000, decimal_places=1, null=True, verbose_name='Задайте цену')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Вставьте файл с картинкой')
    music = models.FileField(upload_to='nusic/', null=True, blank=True, verbose_name='Вставьте музыку ')
    type_books = models.CharField(max_length=100, choices=TYPE_BOOKS_CHOICES, null=True, verbose_name='Выберите жанр книги')
    youtube_url = models.URLField(null=True, blank=True, verbose_name='Вставьте url ссылку YouTube ролика')
    full_description = models.TextField(null=True, verbose_name='Напишите полное описание книги')
    autor = models.CharField(max_length=100, null=True, verbose_name='Напишите имя автора')
    tags = models.ManyToManyField(BookTag, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'
