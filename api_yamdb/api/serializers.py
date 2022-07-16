from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Comment, Review, User, SCORES


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'review', 'text', 'created')
        read_only_fields = ('id', 'created', 'review', 'author')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    score = serializers.ChoiceField(choices=SCORES)

    class Meta:
        model = Review
        fields = ('id', 'author', 'score', 'title', 'text', 'created')
        read_only_fields = ('id', 'created', 'title', 'author')
