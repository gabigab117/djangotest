from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from . import mail_notification


User = get_user_model()


@receiver(post_save, sender='account.Claim')
def notify_user(sender, instance, created, **kwargs):
    """
    Notifies the user about the status change of their claim.
    """
    if not created:
        mail_notification.user_notification_claim_status_change(instance)


@receiver(post_save, sender='account.Claim')
def notify_managers(sender, instance, created, **kwargs):
    """
    Notifies managers about a new claim.
    """
    if created:
        mail_notification.manager_notification_new_claim(instance)


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    """
    Sends a welcome email to the user.
    """
    if created:
        mail_notification.welcome_email(instance)