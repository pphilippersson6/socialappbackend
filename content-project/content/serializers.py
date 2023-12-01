from rest_framework import serializers
from .models import *

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    user=UserListSerializer()
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class FollowListSerializer(serializers.ModelSerializer):
    user=UserListSerializer()
    followed_user=UserListSerializer()
    class Meta:
        model = Follow
        fields = '__all__'

class PostLikesSerializer(serializers.ModelSerializer):
    user=UserListSerializer()
    class Meta:
        model = Like
        fields = '__all__'
