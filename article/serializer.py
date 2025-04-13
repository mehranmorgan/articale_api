from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment, Article


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ArticelSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, required=False)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    article = ArticelSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


