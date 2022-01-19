from django.db import models
from datetime import datetime
from core.abstractions.model_abstract import CreationDateAbstract


class CustomUser(CreationDateAbstract):
    """ User info model """
    email = models.EmailField()
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    """ fields for control user """

class Organistaion(models.Model):
    """ organisation model """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organistaion')
    unp = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    org_email = models.EmailField(blank=True, null=True)
    site = models.URLField(default='', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    time_graf = models.TextField(blank=True, null=True)
    socials = models.JSONField(blank=True, null=True)







