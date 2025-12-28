from django.contrib.auth.models import AbstractUser
from django.db import models


def user_avatar_upload_path(instance, filename):
    return f"users/{instance.username}/{filename}"


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to=user_avatar_upload_path,
        blank=True,
        null=True,
        verbose_name="Аватар"
    )
    
    bio = models.TextField(blank=True, null=True, verbose_name="О себе")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"