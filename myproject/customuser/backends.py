from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from customuser.models import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        return CustomUser.objects.filter(username=username,password=password).first()

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None