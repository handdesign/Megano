from django.contrib.auth.models import User
from django.db import models


def avatar_directory_path(instance: 'Profile', filename: str) -> str:
    return 'avatars/avatar_{pk}/avatar/{filename}'.format(
        pk=instance.pk,
        filename=filename
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to=avatar_directory_path, blank=True)

    def __str__(self):
        return self.fullName
