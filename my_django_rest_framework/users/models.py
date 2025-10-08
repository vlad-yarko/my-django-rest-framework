from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# from PIL import Image

# Create your models here.

class CustomUser(AbstractUser):
    """Our implementation of Base Django User Model"""
    email = models.EmailField(_("email address"), blank=True, unique=True)

    # bio = models.TextField(
    #     max_length=500,
    #     blank=True,
    #     verbose_name="Коротка біографія"
    # )


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    first_login_completed = models.BooleanField(default=False)
    # birth_date = models.DateField(null=True, blank=True)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Профіль {self.user.username}"

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"
