from allauth.account.models import EmailAddress
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email should be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        if user.is_superuser:
            EmailAddress.objects.create(
                user=user, email=email, primary=True, verified=True
            )

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise Exception("Superuser must have is_staff set at true")

        if extra_fields.get("is_superuser") is not True:
            raise Exception("Superuser must have is_superuser set at true")

        return self._create_user(email, password, **extra_fields)


def user_directory_path(instance, filename):
    return f"users/{instance.id}/{filename}"


class AccountType(models.TextChoices):
    # Just here so that it can be extended easily later
    GENERAL = "general", _("General")
    STAFF = "staff", _("Staff")


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(
        upload_to=user_directory_path,
        name="profile_pic",
        blank=True,
        null=True,
    )
    account_type = models.CharField(
        choices=AccountType.choices, default=AccountType.GENERAL, max_length=8
    )
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.name
