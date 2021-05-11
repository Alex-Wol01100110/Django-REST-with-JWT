from django.contrib.auth.middleware import get_user
from django.utils.functional import SimpleLazyObject
from django.utils import timezone

from rest_framework.request import Request
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Profile


class UpdateLastActivityMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            Profile.objects.filter(user__id=request.user.id) \
                           .update(last_activity=timezone.now())



class CustomSimpleJWTMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            request.user = authentication.JWTAuthentication().authenticate(
                                                                request)[0]
        except Exception as e:
            pass



"""
class AuthenticationMiddlewareJWT(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda: self.__class__.get_jwt_user(request))
        print(f'user! = {request.user}')
        return self.get_response(request)

    @staticmethod
    def get_jwt_user(request):
        user = get_user(request)
        if user.is_authenticated:
            return user
        try:
            #request.user = authentication.JWTAuthentication().
            #                                        authenticate(request)[0]
            user_jwt = authentication.JWTAuthentication()().authenticate(request)[0]
            #if user_jwt is not None:
            #    return user_jwt[0]
        except Exception as e:
            print(f'Exception = {e}')
        return user # AnonymousUser

"""
