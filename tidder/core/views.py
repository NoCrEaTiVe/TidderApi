from django.shortcuts import render
from rest_framework.response import Response
from core import serializers
from rest_framework import generics, authentication, permissions, viewsets, mixins, status
from .models import *


class PostViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return self.queryset
