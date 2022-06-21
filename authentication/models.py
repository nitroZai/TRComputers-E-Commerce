from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    is_seller = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


