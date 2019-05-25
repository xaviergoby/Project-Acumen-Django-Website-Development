from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class CustomUser(AbstractUser):
    # My CustomUserModel

    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(unique=True, null=True, blank=True, max_length=50)
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    educational_institution_name = models.CharField(null=True, blank=True, max_length=50)
    educational_level = models.CharField(null=True, blank=True, max_length=50)

    # def __str__(self):
    #     return self.user.user