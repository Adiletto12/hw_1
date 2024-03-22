from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Как вас зовут?')
    email = models.EmailField(verbose_name='Укажите вашу почту', blank=True)
    description = models.TextField(verbose_name='Напишите комментарий', null=True)

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'Добавить комментарий'
    verbose_name_plural = 'Комментарии'
