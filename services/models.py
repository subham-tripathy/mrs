from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)


class YourModel(AbstractUser):
    username = models.CharField(max_length=100, unique=True, default='')
    email = models.EmailField(default='')
    password = models.CharField(max_length=100, default='')
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class comments(models.Model):
    user=models.CharField(default='', max_length=100)
    film=models.CharField(default='', max_length=100)
    comment=models.CharField(default='', max_length=100)
    rating=models.IntegerField()