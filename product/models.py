from django.db import models

class Teg(models.Model):
    name = models.CharField(max_length=100, verbose_name='напишите тег',default='#')

    def __str__(self):
        return f'#{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    tags = models.ManyToManyField(Teg)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.tags}'