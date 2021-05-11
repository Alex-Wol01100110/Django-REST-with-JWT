from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_class = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    User = get_user_model()
    query = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserLastLoginAndLastRequestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        User = get_user_model()
        current_user = User.objects.get(id=request.user.id)
        last_login = current_user.last_login 
        print(f'last login = {last_login}')
        
        last_activity = current_user.profile.last_activity
        print(f'last_act = {last_activity}')

        return Response(last_login)
        
