from django.db import models
from uuid import uuid4


class CreationDateAbstract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)


class CustomUser(models.Model):
    """ User info model """
    PYMENT_STATUS = (
        ('free', 'free'),
        ('month', 'month'),
        ('year', 'year'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True, default='your name')
    last_name = models.CharField(max_length=255, blank=True, null=True)
    """ fields for control user """
    payment_status = models.CharField(max_length=10, default='free', blank=True, null=True)
    pays = models.DecimalField(default=20, decimal_places=2, max_digits=10, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    """ organization model """

    TYPE_ORGANISATION = (
        ('sale', 'sale'),
        ('rent', 'rent'),
        ('repair', 'repair'),
    )

    name = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organisation', blank=True, null=True)
    unp = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    org_email = models.EmailField(blank=True, null=True)
    site = models.URLField(default='', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    time_graf = models.TextField(blank=True, null=True, verbose_name='График работы')
    socials = models.JSONField(blank=True, null=True, verbose_name='Social')
    org_type = models.CharField(max_length=15, choices=TYPE_ORGANISATION, default='rent', blank=True, null=True)


class Favorite(CreationDateAbstract):
    """ favorite ad or organisation by user """

    FAVORITE_CHOICE = (
        ('ad', 'ad'),
        ('org', 'org'),
    )
    favorite_type = models.CharField(max_length=5, choices=FAVORITE_CHOICE, default='ad')
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='favorites', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    org = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
