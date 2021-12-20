from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.sessions.models import Session
from django.utils import timezone
from digifix_computer_repair.settings import AUTH_USER_MODEL


class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, password):
        user = self.model(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email", unique=True, max_length=255, blank=True, null=True)
    username = models.CharField("User Name", unique=True, max_length=255, blank=True, null=True)
    profile_image = models.FileField(upload_to='profile_image', blank=True, null=True)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Staff', default=False)
    is_engineer = models.BooleanField('Engineer', default=False)
    is_customer = models.BooleanField('Customer', default=False)
    is_superuser = models.BooleanField('Super User', default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "User"


