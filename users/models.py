from django.db import models

from django.contrib.auth.models import AbstractUser

class ExtendUSer(AbstractUser):
    email = models.EmailField(max_length=250, blank=True, verbose_name='email')
    
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"