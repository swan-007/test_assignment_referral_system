from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class PhoneNumberUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not phone_number:
            raise ValueError('The given phone number must be set')
        user = self.model(
             phone_number=phone_number,
             **extra_fields
        )
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number,
                                 **extra_fields)

    def create_superuser(self, phone_number,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number,
                                 **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone_number'
    objects = PhoneNumberUserManager()
    phone_number = models.CharField(max_length=12, unique=True)
    username = models.CharField(max_length=50, null=True, unique=False)
    invite_code = models.CharField(max_length=6, null=True)
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    def __str__(self):
        return f'{self.phone_number}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Список пользователей"
        ordering = ('phone_number',)


class PhonCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phone_sms_code')
    phon_code = models.IntegerField(null=True)



class AlienInviteCode(models.Model):
    owner_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='owner_code')
    code_user = models.OneToOneField(User, on_delete=models.CASCADE,
                                     related_name='alien_invite_code',
                                     null=True)
    code = models.CharField(max_length=6)




