from django.db import models

from django.apps import apps
from django.conf import settings
from django.db import models
from django .contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _



class DefaultLevels(TimeStampedModel):
    class DefaultLeve(models.IntegerChoices):
        """
            This is a class for UserLeve choices.
        """
        LEVEL1 = 1, _('LEVEL 1')
        LEVEL2 = 2, _('LEVEL 2')
        LEVEL3 = 3, _('LEVEL 3')
        LEVEL4 = 4, _('LEVEL 4')
        LEVEL5 = 5, _('LEVEL 5')
        LEVEL6 = 6, _('LEVEL 6')
        LEVEL7 = 7, _('LEVEL 7')

    level = models.IntegerField(choices=DefaultLeve.choices, default=DefaultLeve.LEVEL1, unique=True)
    convert = models.BigIntegerField(default=0)
    deposit_irr = models.BigIntegerField(default=0)
    deposit_crypto = models.BigIntegerField(default=0)
    withdraw_irr = models.BigIntegerField(default=0)
    withdraw_crypto = models.BigIntegerField(default=0)
    buy = models.BigIntegerField(default=0)
    sell = models.BigIntegerField(default=0)
    turnover = models.BigIntegerField(default=0)


class UserLevel(TimeStampedModel):
    class UserLeve(models.IntegerChoices):
        """
            This is a class for UserLeve choices.
        """
        LEVEL1 = 1, _('LEVEL 1')
        LEVEL2 = 2, _('LEVEL 2')
        LEVEL3 = 3, _('LEVEL 3')
        LEVEL4 = 4, _('LEVEL 4')
        LEVEL5 = 5, _('LEVEL 5')
        LEVEL6 = 6, _('LEVEL 6')
        LEVEL7 = 7, _('LEVEL 7')

    level = models.IntegerField(choices=UserLeve.choices, default=UserLeve.LEVEL1)
    convert = models.BigIntegerField(default=0)
    deposit_irr = models.BigIntegerField(default=0)
    deposit_crypto = models.BigIntegerField(default=0)
    withdraw_irr = models.BigIntegerField(default=0)
    withdraw_crypto = models.BigIntegerField(default=0)
    buy = models.BigIntegerField(default=0)
    sell = models.BigIntegerField(default=0)
    turnover = models.BigIntegerField(default=0)


# class CustomUserManager(UserManager):
#     use_in_migrations = True

#     def _create_user(self, phone_number, password, **extra_fields):
#         """
#         Create and save a user with the given phone_number and password.
#         """

#         if not phone_number:
#             raise ValueError("The given phone_number must be set")

#         GlobalUserModel = apps.get_model(
#             self.model._meta.app_label, self.model._meta.object_name
#         )
#         user = self.model(phone_number=phone_number, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, phone_number, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(phone_number, password, **extra_fields)

#     def create_superuser(self, phone_number, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser, TimeStampedModel):

    class UserMainInfoCheck(models.TextChoices):
        IN_PROGRESS = "inprogress", _('in progress')
        MATCHED = "matched", _('matched')
        FAILED = "failed", _('failed')
    username = models.CharField(max_length=20, unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    balance_chart = models.JSONField(null=True, blank=True)
    level = models.OneToOneField("UserLevel", on_delete=models.CASCADE, null=True, blank=True)
    auth_info = models.OneToOneField("UserAuthInfo", on_delete=models.CASCADE, null=True, blank=True)
    send_with_sms = models.BooleanField(default=True)
    send_with_email = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="media/avatars", null=True, blank=True)
    approve_rules = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    otp_enabled = models.BooleanField(default=False)
    otp_verified = models.BooleanField(default=False)
    otp_base32 = models.CharField(max_length=255, null=True, blank=True)
    otp_auth_url = models.CharField(max_length=255, null=True, blank=True)
    is_blocked = models.BooleanField(default=False, null=True, blank=True)
    change_password_time = models.DateTimeField(blank=True, null=True)
    user_main_info_check_status = models.CharField(max_length=12, choices=UserMainInfoCheck.choices,
                                                   default=UserMainInfoCheck.IN_PROGRESS, null=True, blank=True)
    user_main_info_check_status_msg = models.TextField(null=True, blank=True)
    user_card_info_check_status = models.CharField(max_length=20, choices=UserMainInfoCheck.choices,
                                                   default=UserMainInfoCheck.IN_PROGRESS, null=True, blank=True)
    user_card_info_check_status_msg = models.TextField(null=True, blank=True)
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        # indexes = [
        #     models.Index(fields=['published'], name='published_idx', condition=Q(published=True))
        # ]
        # indexes = [
        #     models.Index(fields=['first_name', 'last_name'])
        # ]

    def __str__(self):
        if self.get_full_name:
            return '{} ({})'.format(self.full_name, self.phone_number.__str__())
        return self.phone_number.__str__()
    
    
    

class UserAuthInfo(TimeStampedModel):

    class Gender(models.TextChoices):
        MALE = 'male', _('MALE')
        FEMALE = 'female', _('FEMALE')

    kyc_completed = models.BooleanField(default=False, null=True, blank=True)
    kyc_verified = models.BooleanField(default=False, null=True, blank=True)
    nation_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)   
    card_image = models.ImageField(upload_to="auth/card_image", null=True, blank=True)
    backside_card_image = models.ImageField(upload_to="auth/backside_card_image", null=True, blank=True)
    verification_video = models.FileField(upload_to="auth/verification_video", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.FEMALE)
    job = models.CharField(max_length=100, default='Trader', null=True, blank=True)
    approximate_monthly_deposit = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
    


class UserBankInfo(TimeStampedModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="banks")
    account_card_number = models.CharField(max_length=16, unique=True, null=True, blank=True)
    iban = models.CharField(max_length=30, null=True, blank=True)


class KYCResult(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    nation_code_result = models.BooleanField(default=False, null=False, blank=True)
    birth_date_result = models.BooleanField(default=False, null=False, blank=True)
    account_card_number_result = models.BooleanField(default=False, null=False, blank=True)
    card_image_result = models.BooleanField(default=False, null=False, blank=True)
    backside_card_image_result = models.BooleanField(default=False, null=False, blank=True)
    verification_video_result = models.BooleanField(default=False, null=False, blank=True)

    @classmethod
    def create(cls, user):
        return cls.objects.get_or_create(user=user)
