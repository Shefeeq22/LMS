from django.shortcuts import render,get_object_or_404

from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.response import Response

from accounts.serializer import UserSerializer
from accounts.models import User
from accounts.serializer import UserSerializer,TrainerProfileSerilaizer
from accounts.permissions import IsOwner
from accounts.models import TrainerProfile

# Create your views here.
class UserCreateView(CreateAPIView):

    serializer_class = UserSerializer

class AuthUserDetailView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def get(self,request):

        user_object = User.objects.get(id = request.user.id)

        serializer_instance = UserSerializer(user_object)

        return Response(serializer_instance.data)

class TrainerProfileRetrieveUpdateView(RetrieveUpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = TrainerProfileSerilaizer

    def get_queryset(self):

        return TrainerProfile.objects.filter(trainer_id = self.request.user)

    



    