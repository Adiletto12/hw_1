from django.db import models

class Parser(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title