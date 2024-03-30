from django.db import models

class MashinaParser(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.title
