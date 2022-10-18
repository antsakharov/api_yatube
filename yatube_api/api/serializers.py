from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели Group"""
    class Meta:
        model = Group
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post"""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Comment"""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
