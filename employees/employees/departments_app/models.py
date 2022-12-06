from django.contrib.auth import get_user_model
from django.db import models


class Department(models.Model):
    TITLE_MAX_LENGTH = 15
    CATEGORIES = [
        ('C1', 1),
        ('C2', 2),
        ('C3', 3),
    ]

    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)

    created_on = models.DateField(auto_now=True)

    category = models.CharField(max_length=3, choices=CATEGORIES)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title}'
