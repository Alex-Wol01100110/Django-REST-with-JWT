
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import PostCreateSerializer

from ..models import Post, Like


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostCreateSerializer


class PostLikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, id=pk)
        if post.likes.all().filter(user=request.user).exists():
            return Response({'liked': False})
        else:
            newlike = Like.objects.create(user=request.user, post=post)
            return Response({'liked': True})


class PostUnlikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, id=pk)
        if post.likes.all().filter(user=request.user).exists():
            like = Like.objects.all().filter(post=post, user=request.user)
            like.delete()
            return Response({'unliked': True})
        else:
            return Response({'unliked': False})


class TotalLikesByDatesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request, date_from, date_to, format=None):
        """Return list of all likes in certain time gap."""
        likes_range = list()
        likes_range.append(date_from)
        likes_range.append(date_to)
        total_likes = Like.objects.all().filter(
                            updated__range=likes_range).count()
        return Response(total_likes)



