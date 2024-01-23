from django.db import models


class Category(models.Model):
    categoryname = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self) -> str:
        return self.categoryname


class Product(models.Model):
    name = models.CharField(max_length=30, null=True,blank=True)
    price = models.CharField(max_length=40,null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name