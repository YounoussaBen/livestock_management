from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

# Add related_name to prevent clashes with built-in User model
User._meta.get_field('groups').remote_field.related_name = 'custom_user_set'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_set_permissions'
