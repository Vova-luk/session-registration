
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class Reg(AbstractUser):
    username = None
    patronymic=models.CharField(max_length=40, validators=(MinLengthValidator(3),),blank=True,default='')
    email=models.EmailField(max_length=250, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()
    def __str__(self):
        return f'{self.last_name} - {self.first_name} - {self.email}'

