from django.shortcuts import render

from rest_framework.generics import CreateAPIView

from accounts.serializer import UserSerializer

# Create your views here.
class UserCreateView(CreateAPIView):

    serializer_class = UserSerializer