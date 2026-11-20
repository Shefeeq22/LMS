from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework import authentication

from education.serializers import CourseSerializer
from education.permissions import IsTrainer
from education.models import Course

# Create your views here.
class CourseListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsTrainer]

    serializer_class = CourseSerializer

    def get_queryset(self):

        return Course.objects.filter(trainer = self.request.user)

    def perform_create(self, serializer):
        
        serializer.save(trainer = self.request.user)