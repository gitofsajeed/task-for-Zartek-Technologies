from rest_framework import serializers
from .models import Post, Image, Tag, Like

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'weight']


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    liked_users = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'images', 'description', 'tags', 'likes_count', 'dislikes_count', 'liked_users', 'created_date']

    def get_likes_count(self, instance):
        return Like.objects.filter(post=instance, like_status=True).count()

    def get_dislikes_count(self, instance):
        return Like.objects.filter(post=instance, like_status=False).count()

    def get_liked_users(self, instance):
        liked_users = Like.objects.filter(post=instance, like_status=True).values_list('user__username', flat=True)
        return liked_users


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'post', 'like_status']

