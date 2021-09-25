from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defaut.jpg', upload_to='profile_image')

    def __str__(self):
        return f'{self.user.username} profile image'
