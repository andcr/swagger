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
class MyQueue:
  def __init__(self):
    self.input = []
    self.output = []

  def push(self, x: int) -> None:
    self.input.append(x)

  def pop(self) -> int:
    self.peek()
    return self.output.pop()

  def peek(self) -> int:
    if not self.output:
      while self.input:
        self.output.append(self.input.pop())
    return self.output[-1]

  def empty(self) -> bool:
    return not self.input and not self.output