from django.utils import timezone

from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Profile


class UpdateLastActivityMiddleware(object):
    """
        Update user activity, if user is authenticated.
    """

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
    """
        Authenticate user by token.
    """

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

