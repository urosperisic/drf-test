from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, null=True)

    @property
    def role(self):
        return 'admin' if self.is_superuser else 'user'

    def __str__(self):
        return self.username