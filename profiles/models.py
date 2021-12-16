from django.db import models
# https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining reservation history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    default_phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True
    )  # validators should be a list

    def __str__(self):
        return self.user.username


# receiver to create or update a user every time a user object is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
