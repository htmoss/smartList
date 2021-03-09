from django.db import models


class FoodType(models.Model):
    type = models.CharField(max_length=200, default="",
                            help_text='Think different sections of the grocery store, like meat, bread, or vegetables')

    def __str__(self):
        return self.type


# class Metric(models.Model):
#     metric = models.CharField(max_length=20, default="", unique=True)

#     def __str__(self):
#         return self.metric


class Ingredient(models.Model):
    name = models.CharField(max_length=200, default="",
                            unique=True, primary_key=True)
    # ing_have = models.BooleanField(blank=False)
    amount = models.IntegerField(default=1)
    # metric = models.ForeignKey(Metric, on_delete=models.CASCADE, default="")
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
