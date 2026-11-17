from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):

    phone = models.CharField(max_length = 15,unique = True)

    role = models.CharField(max_length = 100)

class StudentProfile(models.Model):

    email_address = models.EmailField(null = True)

    phone_number = models.PositiveIntegerField(null = True)

    date_of_birth = models.DateField(null = True)

    GENDER_CHOICES = (
        ("male","male"),
        ("female","female")
    )

    gender = models.CharField(max_length = 100,choices = GENDER_CHOICES,default = "male")

    profile_picture = models.ImageField(upload_to = "profile_pictures",null = True)

    owner = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "profile")

class TrainerProfile(models.Model):

    email = models.EmailField(null = True)

    phone_number = models.PositiveIntegerField(null = True)

    profession = models.CharField(max_length = 100,null = True)

    experience = models.CharField(max_length = 100,null = True)

    owner = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "proflies")

def create_user_profile(sender,instance,created,**kwargs):

    if created:

        StudentProfile.objects.create(owner = instance)

post_save.connect(create_user_profile,sender = User)

def create_trainer_profile(sender,instance,created,**kwargs):

    if created:

        TrainerProfile.objects.create(owner = instance)

post_save.connect(create_trainer_profile,sender = User)