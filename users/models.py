from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, isAdmin, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(
            first_name=first_name,
            isAdmin=isAdmin,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, first_name, isAdmin, email, password=None):
        user = self.create_user(
            first_name,
            isAdmin,
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    isAdmin = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
        
    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name']

    def _str_(self):
        return self.email
    
User = get_user_model()

class ItemPhoto(models.Model):
    itemPhoto = models.ImageField(upload_to='images/')
    shortName = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    arivel = models.CharField(max_length=255, default="")
    sale = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    haracteristic = models.TextField()

    def __str__(self):
        return f"Photos for {self.user.email}"
    
class UserBuy(models.Model):
    user_name = models.IntegerField(max_length=255)
    item = models.IntegerField(max_length=255)

    
    def __str__(self):
        return f"Photos for"
    
