from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from rest_framework import authentication

from education.serializers import CourseSerializer
from accounts.permissions import IsOwner
from education.models import Course

# Create your views here.
class CourseListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = CourseSerializer

    def get_queryset(self):
        
        return Course.objects.filter(trainer = self.request.user)

    def perform_create(self, serializer):
        
        serializer.save(trainer = self.request.user)

class CourseRetrieveUpdateView(RetrieveUpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = CourseSerializer

    def get_queryset(self):
    
        return Course.objects.filter(trainer = self.request.user)