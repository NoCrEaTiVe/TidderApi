from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','user','title','community','text','rating','image')
        read_only_fields = ('id',)
