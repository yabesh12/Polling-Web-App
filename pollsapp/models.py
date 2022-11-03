from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    mobile_no = models.PositiveIntegerField()
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"


class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option


class Contestant(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField('uploads/participants')
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.user.username}"
