from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if email is None:
            raise Exception("User must have an email")

        user = self.model(email=self.normalize_email(email), *kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        if email is None:
            raise Exception("User must have an email")

        user = self.create_user(email, password, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(
            verbose_name="Email address",
            max_length=128,
            unique=True,
            db_index=True,
            null=False,
            blank=False
        )
    password = models.CharField(verbose_name="Passwd", max_length=128)
    reg_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    sur_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return bool(self.is_admin)
