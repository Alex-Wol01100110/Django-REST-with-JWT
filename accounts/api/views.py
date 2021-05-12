from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    """
       Authenticate user and set last login time. 
    """
    permission_class = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """
        Register user.
    """

    User = get_user_model()
    query = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserLastLoginAndLastRequestView(APIView):
    """
        Return user's last login time and
        last activity time.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        User = get_user_model()
        current_user = User.objects.get(id=request.user.id)
        last_login = current_user.last_login 
        
        last_activity = current_user.profile.last_activity

        return Response(f'last login {last_login} last request {last_activity}')
        
