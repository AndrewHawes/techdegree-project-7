import os

from ckeditor.fields import RichTextField
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email
from django.db import models

from .fields import DatePickerField
from .managers import CustomUserManager
from imageutils.models import Photo


def image_path(instance, filename):
    return os.path.join('images', str(instance.username), filename)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, validators=[validate_email])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = DatePickerField(verbose_name='Date of birth')
    bio = RichTextField()
    avatar = models.ImageField(upload_to=image_path, verbose_name='User avatar')
    favorite_animal = models.CharField(max_length=50, blank=True)
    hobbies = models.CharField(max_length=100, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []  # allow superuser creation without extra fields

    def __str__(self):
        return '@{}'.format(self.username)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

