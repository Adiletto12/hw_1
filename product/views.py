from django.shortcuts import render
from django.views import generic
from . import models
class ProductListView(generic.ListView):
    template_name = 'product/product_list.html'
    context_object_name = 'product'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

class MealListView(generic.ListView):
    template_name = 'product/meal_list.html'
    context_object_name = 'meal'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='еда').order_by('-id')