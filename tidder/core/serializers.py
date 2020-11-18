from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user','community','title','text','rating','image']
        read_only_fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','user','text','post','rating')
        read_only_fields = ('id',)


class PostDetailSerializer(serializers.ModelSerializer):
    comment = CommentSerializer()
    class Meta:
        model = Post
        fields = ['id','user','community','title','text','rating','image']
        read_only_fields = ('id',)
        depth = 1


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id','name','description')
        read_only_fields = ('id',)
