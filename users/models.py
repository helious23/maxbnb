from django.contrib.auth.models import AbstractUser
from django.db import models

# AbstractUser class : admin 패널에서 사용중인 user class
# 이후 성별, 주소 등등 추가해주기 위해 새롭게 모델링


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "한국어"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = ((CURRENCY_USD, "$USD"), (CURRENCY_KRW, "₩원"))

    # upload_to : setting 에서 지정한 media_root 안에 세부 폴더 지정할 수 있음
    avatar = models.ImageField(blank=True, upload_to="avatars")
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
    )  # max_length 는 필수
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=3,
        blank=True,
    )
    superhost = models.BooleanField(default=False)
