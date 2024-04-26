from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoUserModel
from django.utils.translation import gettext_lazy as _

"""
	TODO documentation.
"""
class User(DjangoUserModel):
     class Meta:
        ordering = ["date_joined"]