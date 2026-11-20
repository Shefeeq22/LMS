from django.db import models

from accounts.models import User

# Create your models here.
class Course(models.Model):

    title = models.CharField(max_length = 100)

    description = models.TextField(null = True)

    duration = models.FloatField()

    fee = models.PositiveIntegerField()

    cover_picture = models.ImageField(null = True)

    trainer = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "courses")
