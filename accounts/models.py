from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, email, account_id, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, account_id=account_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, account_id, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, account_id, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )

class User(AbstractBaseUser, PermissionsMixin):
    account_id = models.CharField(
        verbose_name="アカウントID",
        unique=True,
        max_length=10,
    )
    email = models.EmailField(
        verbose_name="メールアドレス",
        unique=True
    )
    first_name = models.CharField(
        verbose_name="名",
        max_length=150,
        null=True,
        blank=False
    )
    last_name = models.CharField(
        verbose_name="姓",
        max_length=150,
        null=True,
        blank=False
    )
    birth_date = models.DateField(
        verbose_name="生年月日",
        blank=True,
        null=True
    )
    is_superuser = models.BooleanField(
        verbose_name="スーパーユーザー",
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name='スタッフステータス',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='アクティブ',
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name="作成日",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="更新日",
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'account_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.account_id