from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import CustomUser, Organization


@receiver(post_save, sender=CustomUser)
def create_organisation(sender: CustomUser, instance: object, created: bool, **kwargs: dict):
    organisation_create = Organization.objects.create(user=instance)


