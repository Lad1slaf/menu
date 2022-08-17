from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_file_extension

E = 'Employee'
R = 'Restaurant'
ROLE_CHOICES = (
    (E, "Employee"),
    (R, "Restaurant"),
)


class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Restaurant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='restaurant_admin')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    menu = models.FileField(validators=[validate_file_extension], upload_to='uploads/%Y/%m/%d/')
    date = models.DateField(auto_now_add=True)

    @property
    def vote_count(self):
        vote = Vote.objects.filter(menu=self.pk).count()
        return vote


class Vote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='votes')
    date = models.DateField(auto_now_add=True)
