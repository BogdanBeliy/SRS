from django.db import models
from datetime import datetime
from core.abstractions.model_abstract import CreationDateAbstract


class Category(CreationDateAbstract):
    """ Category model """
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание')


class SubCategory(CreationDateAbstract):
    """ SubCategory model """
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')


class Advertisement(CreationDateAbstract):
    """ Advertisement model """
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='advertisement')
    photo = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание объявления')




