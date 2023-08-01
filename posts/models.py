from django.db import models
from django.contrib.auth import get_user_model


class Theme(models.Model):
    name = models.CharField(max_length=250, primary_key=True)

    def __str__(self) :
        return self.name


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='postsapp_img')
    themes = models.ManyToManyField(Theme, null=True, blank=True)

    def __str__(self):
        return self.title