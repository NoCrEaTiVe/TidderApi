"""tidder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostView.as_view({'get':'list','post':'create'})),
    path('posts/', PostView.as_view({'patch':'update','delete':'destroy'})),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('posts/<int:id>/comments/', CommentView.as_view()),
    path('community/', CommunityView.as_view({'get':'list','post':'create'})),
    path('community/<int:pk>/', CommunityView.as_view({'patch':'update','delete':'destroy'})),
    path('community/<int:id>/posts/', PostsByCommunity.as_view()),
    path('comments/', CommentList.as_view({'get':'list','post':'create'})),
    path('comments/<int:pk>', CommentList.as_view({'patch':'update','delete':'destroy'})),
    path('comments/<int:id>/', CommentDetailView.as_view()),
]
