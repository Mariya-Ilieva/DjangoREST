from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from employees.departments_app.models import Department
from employees.employees_app.validators import validate_name, validate_phone_number


class Director(UserManager):
    pass


class Employee(AbstractUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 15
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True,
                                validators=[MinLengthValidator(4), ])

    email = models.EmailField(unique=True)

    date_joined = models.DateField(auto_now_add=True)

    age = models.PositiveIntegerField(validators=[MinValueValidator(18), ])

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=[validate_name, ])

    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,
                                 validators=[validate_name, ])

    phone_number = models.CharField(max_length=10, validators=[validate_phone_number, ])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'age', 'first_name', 'last_name']

    objects = Director()
