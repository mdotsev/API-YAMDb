import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
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


class Category(models.Model):
    name = models.CharField('Название', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Название', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Название', max_length=256)
    year = models.PositiveIntegerField(
        verbose_name='Дата выхода',
        validators=[MaxValueValidator(datetime.date.today().year)]
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        default=None
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    genre = models.ManyToManyField(Genre, through='GenreTitle')

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, жанр - {self.genre}'
