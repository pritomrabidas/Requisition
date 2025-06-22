from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ROLE_COICES =(
        ("admin","Admin"),
        ("manager","Manager"),
        ("employ","Employ"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_COICES, default="employ")
    

    def __str__(self):
        return f'{self.user.username} - {self.role}'
