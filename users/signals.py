from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User, Member


@receiver(post_save, sender=User)
def create_member_profile(sender, instance, created, **kwargs):
    if created:
        if not instance.is_staff and not instance.is_superuser:
            Member.objects.create(user=instance)
