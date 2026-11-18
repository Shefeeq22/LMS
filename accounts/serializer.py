from rest_framework import serializers

from accounts.models import User
from accounts.models import TrainerProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password","phone","role"]

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)

class TrainerProfileSerilaizer(serializers.ModelSerializer):

    class Meta:

        model = TrainerProfile

        fields = "__all__"