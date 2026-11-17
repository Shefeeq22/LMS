from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):

    ROLE_CHOICES = (
        ("Trainer","Trainer"),
        ("Student","Student")
    )

    phone = models.CharField(max_length = 15,unique = True)

    role = models.CharField(max_length = 100,choices = ROLE_CHOICES)

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

    student_id = models.OneToOneField(User,on_delete = models.CASCADE,related_name = "student_profile")

class TrainerProfile(models.Model):

    email = models.EmailField(null = True)

    phone_number = models.PositiveIntegerField(null = True)

    profession = models.CharField(max_length = 100,null = True)

    experience = models.CharField(max_length = 100,null = True)

    trainer_id = models.OneToOneField(User,on_delete = models.CASCADE,related_name = "trainer_profile")

def create_profile(sender,instance,created,**kwargs):

    if instance.role == "Student":

        StudentProfile.objects.create(student_id = instance)

    elif instance.role == "Trainer":

        TrainerProfile.objects.create(trainer_id = instance)

post_save.connect(create_profile,sender = User)



