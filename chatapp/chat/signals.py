from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Profile
from django.core.mail import send_mail
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Message)
def notify_users(sender, instance, created, **kwargs):
    if created:
        members = instance.chat_room.members.all()
        for user in members:
            if user != instance.user:
                send_mail(
                    'New Message in Chat Room',
                    f'{instance.user.username} sent a new message: {instance.content}',
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )