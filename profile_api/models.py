from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    def create_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email=self.normalize_emai(email)#to normalize the emails(@gmail to chaneg to lower case)
        user=self.model(email=email,name=name)#is passed to the model for which the manager is created for

        user.set_password(password)#comes with abstrat user model.to encrypt the password
        user.save(using=self._db)#to specify the db

        return user

    def create_superuser(self,email,name,password):
        """create and save a new super user"""
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'#since we are replacing username with email field
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """return string representation of user"""
        return self.email
