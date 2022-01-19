from django.db import models



class CreationDateAbstract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)


class CustomUser(CreationDateAbstract):
    """ User info model """
    PYMENT_STATUS = (
        ('free', 'free'),
        ('month', 'month'),
        ('year', 'year'),
    )
    email = models.EmailField()
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    """ fields for control user """
    payment_status = models.CharField(max_length=10, default='free')
    pays = models.DecimalField(default=20, decimal_places=2, max_digits=10)
    status = models.BooleanField(default=True)


class Organization(models.Model):
    """ organization model """

    TYPE_ORGANISATION = (
        ('sale', 'sale'),
        ('rent', 'rent'),
        ('repair', 'repair'),
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organisation')
    unp = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    org_email = models.EmailField(blank=True, null=True)
    site = models.URLField(default='', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    time_graf = models.TextField(blank=True, null=True, verbose_name='График работы')
    socials = models.JSONField(blank=True, null=True, verbose_name='Social')
    org_type = models.CharField(max_length=15, choices=TYPE_ORGANISATION, default='rent')


class Favorite(CreationDateAbstract):
    """ favorite ad or organisation by user """

    FAVORITE_CHOICE = (
        ('ad', 'ad'),
        ('org', 'org'),
    )
    favorite_type = models.CharField(max_length=5, choices=FAVORITE_CHOICE, default='ad')
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='favorites')
    name = models.CharField(max_length=255)
    org = models.PositiveIntegerField(default=0)
    url = models.URLField()
