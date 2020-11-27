from django.db.models import fields
from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password', 'rating', 'communities',
            'followers', 'following'
        ]

        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):

        password = validated_data.pop('password')
        user1 = CustomUser()
        user1.set_password(password)
        user1.username = validated_data.pop('username')
        user1.email = validated_data.pop('email')
        user1.save()

        return user1

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        if 'password' in validated_data and not validated_data['password']:
            validated_data.pop('password')
        else:

            instance.password = validated_data.get('password',
                                                   instance.password)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'user', 'community', 'title', 'text', 'rating', 'image'
        ]
        read_only_fields = ('id', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'text', 'post', 'rating')
        read_only_fields = ('id', )


class PostDetailSerializer(serializers.ModelSerializer):
    comment = CommentSerializer()

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'community', 'title', 'text', 'rating', 'image'
        ]
        read_only_fields = ('id', )
        depth = 1


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'name', 'description')
        read_only_fields = ('id', )
