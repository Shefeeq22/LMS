from rest_framework import serializers

from education.models import Course,Module

class CourseSerializer(serializers.ModelSerializer):

    modules = serializers.SerializerMethodField(read_only = True)

    class Meta:

        model = Course

        fields = ["id","title","description","duration","fee","cover_picture","trainer","modules"]

        read_only_fields = ["id","trainer"]

    def get_modules(self,obj):
    
        module_objects = Module.objects.filter(course = obj)
    
        serializer_instance = ModuleSerializer(module_objects,many = True)
    
        return serializer_instance.data

class ModuleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Module

        fields = ["id","title","description","course"]

        read_only_fields = ["id","course"]
