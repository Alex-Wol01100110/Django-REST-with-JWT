
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

"""
class PostLikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        if request.user in post.users_like.all(): 
            return Response({'liked': False})
        else:    
            post.users_like.add(request.user)
            post.total_likes += 1
            post.save()
            return Response({'liked': True})
"""

class PostLikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        print(f'req user!!! = {request.user}') 
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
            print(f'like = {like}')
            like.delete()
            return Response({'unliked': True})
        else:
            return Response({'unliked': False})



class TotalLikesByDatesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    """
    def get(self, request, format=None,
            year_from, month_from, day_from
            year_to, month_to, day_to):
    """

    def get(self, request, date_from, date_to, format=None):
        """Return list of all likes in certain time gap."""
        likes_range = list()
        likes_range.append(date_from)
        likes_range.append(date_to)
        total_likes = Like.objects.all().filter(
                            updated__range=likes_range).count()
        return Response(total_likes)



"""
class PostUnlikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        if request.user in post.users_like.all():     
            post.users_like.remove(request.user)
            post.total_likes -= 1
            post.save()
            return Response({'unliked': True})
        else:
            return Response({'unliked': False})

class PostLikeUnlikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        if request.user in post.users_like.all(): 
            post.users_like.remove(request.user)
            post.total_likes -= 1
            post.save()
            return Response({'unliked': True})
        else:    
            post.users_like.add(request.user)
            post.total_likes += 1
            post.save()
            return Response({'liked': True})
"""
