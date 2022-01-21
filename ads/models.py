from django.db import models
from account.models import Organization


class CreationDateAbstract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    """ Category model """
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание')


class SubCategory(models.Model):
    """ SubCategory model """
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')


class Advertisement(models.Model):
    """ Advertisement model """

    PAYMENT_TYPE = (
        ('free', 'free'),
        ('day', 'day'),
        ('week', 'week'),
        ('month', 'month'),

    )
    creator = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='ad_by_org')
    name = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=5, choices=PAYMENT_TYPE, default='free')
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='advertisement')
    photo = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание объявления')
    cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    additional_equipment = models.JSONField(blank=True, null=True, verbose_name='Дополнительное оборудование')
    characteristic_vehicle = models.JSONField(blank=True, null=True, verbose_name='Характеристики техники')
