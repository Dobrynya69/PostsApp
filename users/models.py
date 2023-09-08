from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    account_image = models.ImageField(upload_to='postsapp_img', null=True, blank=True)
