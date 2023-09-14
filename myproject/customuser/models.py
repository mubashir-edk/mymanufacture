from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        print('--------')
        return self.create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, username, **extra_fields):
        return self.get(username=username)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_user_permissions',
        blank=True,
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employee_groups',
        blank=True,
    )
    
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
