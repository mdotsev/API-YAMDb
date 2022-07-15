from django.contrib.auth.models import AbstractUser
from django.db import models


# Список ролей пользователя
ROLE_CHOISES = (
    ('USER', 'User'),
    ('MODERATOR', 'Moderator'),
    ('ADMIN', 'Admin'),
)


class User(AbstractUser):
    email = models.EmailField(
        'Email адрес',
        unique=True,
        help_text='Обязательное поле. Не более 254 символов.'
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=20,
        choices=ROLE_CHOISES,
        default='USER',
    )
    confirmation_code = models.TextField(
        'Код подтверждения',
        blank=True,
    )

    def __str__(self):
        return self.username
