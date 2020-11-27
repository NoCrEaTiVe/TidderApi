from django.shortcuts import render
from rest_framework.response import Response
from core import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import generics, authentication, permissions, viewsets, mixins, status
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from core.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class PostView(viewsets.GenericViewSet, mixins.ListModelMixin,
               mixins.CreateModelMixin, mixins.UpdateModelMixin,
               mixins.DestroyModelMixin):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return self.queryset


class PostDetailView(APIView):
    def get_object(self, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializer = serializers.PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = self.get_object(id)
        serializer = serializers.PostSerializer(post,
                                                data=request.data,
                                                partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentView(APIView):
    def get(self, request, id):
        comments = Comment.objects.filter(post=id)

        if 'order_by' in request.query_params:
            comments = comments.order_by(request.query_params['order_by'])

        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentDetailView(APIView):
    def get_object(self, id):
        try:
            return serializers.Comment.objects.get(pk=id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, id):
        comment = self.get_object(id)
        serializer = serializers.CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, id):
        comment = self.get_object(id)
        serializer = serializers.CommentSerializer(comment,
                                                   data=request.data,
                                                   partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = self.get_object(id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(viewsets.GenericViewSet, mixins.ListModelMixin,
                  mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return self.queryset


class CommunityView(viewsets.GenericViewSet, mixins.ListModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    serializer_class = serializers.CommunitySerializer
    queryset = Community.objects.all()

    def get_queryset(self):
        return self.queryset


class CommunityDetailView(APIView):
    def get_object(self, id):
        try:
            return Community.objects.get(pk=id)
        except Community.DoesNotExist:
            raise Http404

    def get(self, request, id):
        community = self.get_object(id)
        serializer = serializers.CommunitySerializer(subreddit)
        return Response(serializer.data)

    def put(self, request, id):
        community = self.get_object(id)
        serializer = serializers.SubredditSerializer(community,
                                                     data=request.data,
                                                     partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        community = self.get_object(id)
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostsByCommunity(APIView):
    def get(self, request, id):
        posts = Post.objects.filter(community=id)
        if 'order_by' in request.query_params:
            posts = posts.order_by(request.query_params['order_by'])
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer

    # def get_permissions(self):

    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]