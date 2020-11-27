from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

router = routers.DefaultRouter()
router.register('', CustomUserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(router.urls)),
    path('posts/', PostView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('posts/', PostView.as_view({
        'patch': 'update',
        'delete': 'destroy'
    })),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('posts/<int:id>/comments/', CommentView.as_view()),
    path('community/', CommunityView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('community/<int:pk>/',
         CommunityView.as_view({
             'patch': 'update',
             'delete': 'destroy'
         })),
    path('community/<int:id>/posts/', PostsByCommunity.as_view()),
    path('comments/', CommentList.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('comments/<int:pk>',
         CommentList.as_view({
             'patch': 'update',
             'delete': 'destroy'
         })),
    path('comments/<int:id>/', CommentDetailView.as_view()),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('auth/', include('rest_auth.urls')),
]
