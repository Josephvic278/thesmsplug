from django.db import models
from users.managers import UserManager
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=150, unique=True, db_index=True)
    phone_number = models.CharField(max_length=20, unique=True)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ref_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transaction_pin = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)
    user_verified = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['email', 'phone_number']
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username