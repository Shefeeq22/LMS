from django.shortcuts import render,get_object_or_404

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response

from education.serializers import CourseSerializer
from accounts.permissions import IsOwner
from education.models import Course,Module,Lesson
from education.serializers import ModuleSerializer,LessonSerilaizer

# Create your views here.
class CourseListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = CourseSerializer

    def get_queryset(self):
        
        return Course.objects.filter(trainer = self.request.user)

    def perform_create(self, serializer):
        
        serializer.save(trainer = self.request.user)

class CourseRetrieveUpdateView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = CourseSerializer

    def get_queryset(self):
    
        return Course.objects.filter(trainer = self.request.user)

class ModuleCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def post(self,request,pk = None):

        form_data = request.data

        course_object = get_object_or_404(Course,id = pk)

        serializer_instance = ModuleSerializer(data = form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(course = course_object)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

class ModuleRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = ModuleSerializer

    def get_queryset(self):

        return Module.objects.filter(course__trainer = self.request.user)

class LessonCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [IsOwner]
    
    def post(self,request,pk = None):
    
        form_data = request.data
    
        module_object = get_object_or_404(Module,id = pk)
    
        serializer_instance = LessonSerilaizer(data = form_data)
    
        if serializer_instance.is_valid():
    
            serializer_instance.save(module = module_object)
    
            return Response(serializer_instance.data)
    
        else:
    
            return Response(serializer_instance.errors)

class LessonRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = LessonSerilaizer

    def get_queryset(self):
    
        return Lesson.objects.filter(module__course__trainer = self.request.user)







