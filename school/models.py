from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=255)

class Professor(models.Model):
  name = models.CharField(max_length=255)

class Score(models.Model):
  name = models.CharField(max_length=255)
  professor = models.ForeignKey(Professor, related_name='scores', on_delete=models.CASCADE)
  student = models.ForeignKey(Student, related_name='scores', on_delete=models.CASCADE)
  value = models.IntegerField()