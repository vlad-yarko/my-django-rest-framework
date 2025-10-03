from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class CustomUser(AbstractUser):
    """Our implementation of Base Django User Model"""
    email = models.EmailField(_("email address"), blank=True, unique=True)
    bio = models.TextField(
        max_length=500, 
        blank=True, 
        verbose_name="Коротка біографія"
    )
    location = models.CharField(max_length=300, blank=True, verbose_name="Місце проживання")
    website = models.URLField(max_length=300, blank=True, verbose_name="Вебсайт")
    github_profile = models.URLField(max_length=300, blank=True, verbose_name="Профіль GitHub")
    linkedin_profile = models.URLField(max_length=300, blank=True, verbose_name="Профіль LinkedIn")
    is_available = models.BooleanField(default=True, verbose_name="Доступний для роботи")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Номер телефону")
    
    def __str__(self):
        return self.email

