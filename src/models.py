from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

choice = (
    ('g', 'General Member'),
    ('l', 'Lifetime Member'),
    ('s', 'Super Admin'),
    ('a', 'Admin')
)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    # username = models.CharField(max_length=63)
    # full_name = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    # email
    # created_at = models.DateTimeField(auto_now=True)

    passport = models.CharField(max_length=63, default='')
    date_of_birth = models.DateField()
    city = models.CharField(max_length=63, default='')
    country = models.CharField(max_length=127, default='')
    member_type = models.CharField(choices=choice, max_length=24, default='')

    is_active = models.BooleanField(max_length=255, default=False)
    # date_joined
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Members"

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


