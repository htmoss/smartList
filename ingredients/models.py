from django.db import models


class FoodType(models.Model):
    foodType = models.CharField(max_length=200, default="",
                                help_text='Think different areas of the grocery store, like meat, bread, or vegetables')

    def __str__(self):
        return self.foodType


class Metric(models.Model):
    metric = models.CharField(max_length=20, default="", unique=True)

    def __str__(self):
        return self.metric


class Ingredient(models.Model):
    name = models.CharField(max_length=200, default="",
                            unique=True, primary_key=True)
    amount = models.IntegerField(default=1)
    metric = models.ForeignKey(
        Metric, on_delete=models.CASCADE, default="", blank=True, null=True)
    foodType = models.ForeignKey(
        FoodType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if(self.metric):
            return "{}{} {}".format(self.amount, self.metric, self.name.lower().capitalize())
        else:
            return "{} {}".format(self.amount, self.name.lower().capitalize())
