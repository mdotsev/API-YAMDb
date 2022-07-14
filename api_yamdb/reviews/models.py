from django.contrib.auth import get_user_model
from django.db import models


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


class Title(models.Model):
    pass


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
