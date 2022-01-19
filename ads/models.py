from django.db import models
from datetime import datetime
from account.models import CreationDateAbstract


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

    TYPE_ADVERTISEMENT = (
        ('free', 'free'),
        ('paid', 'paid'),
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    type_advertisement = models.CharField(max_length=5, choices=TYPE_ADVERTISEMENT, default='free')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='advertisement')
    photo = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание объявления')
    cost = models.DecimalField(blank=True, null=True)
    additional_equipment = models.JSONField(blank=True, null=True, verbose_name='Дополнительное оборудование')
    characteristic_vehicle = models.JSONField(blank=True, null=True, verbose_name='Характеристики техники')





