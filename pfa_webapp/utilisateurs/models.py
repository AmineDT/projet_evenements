from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models
from simple_history.models import HistoricalRecords


class UserProfile(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    club_joined = models.ForeignKey('clubs.Clubs', on_delete=models.CASCADE, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password", "is_superuser", "username", "first_name", "last_name"]

    objects = UserManager()
    history = HistoricalRecords()

    def __str__(self):
        return 'Utilisateur: ' + self.email

    def __repr__(self):
        rep = 'Utilisateur(' + self.username + ',' + self.email + ')'
        return rep

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
