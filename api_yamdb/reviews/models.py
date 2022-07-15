import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator

SCORES = (
    (1, "One"),
    (2, "Two"),
    (3, "Three"),
    (4, "Four"),
    (5, "Five"),
    (6, "Six"),
    (7, "Seven"),
    (8, "Eight"),
    (9, "Nine"),
    (10, "Ten"),
)


User = get_user_model()



class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.IntegerField(choices = SCORES)
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='author_title'
            ),
        ]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )


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