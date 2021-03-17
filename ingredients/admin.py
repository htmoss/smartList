from django.contrib import admin
from .models import Ingredient, FoodType, Metric

admin.site.register(Ingredient)
admin.site.register(FoodType)
admin.site.register(Metric)
