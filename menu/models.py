from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=64)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                             related_name='categories')

    def __str__(self):
        return f'{self.menu.name} --> {self.title}'

    class Meta:
        verbose_name_plural = 'Categories'


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item')
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.price}'
