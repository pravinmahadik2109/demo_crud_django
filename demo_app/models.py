from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class SuperadminManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Superadmin users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Superadmin(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = SuperadminManager()

class NormalUser(models.Model):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    password = models.CharField(max_length=255)
