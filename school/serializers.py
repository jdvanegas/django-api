from .models import *
from rest_framework import serializers

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
  student = serializers.PrimaryKeyRelatedField(
    queryset=Student.objects.all())
  professor = serializers.PrimaryKeyRelatedField(
    queryset=Professor.objects.all())
  class Meta:
    model = Score    
    fields = ('id', 'name', 'student', 'professor', 'value')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
  scores = ScoreSerializer(many=True, read_only=True)
  class Meta:
    model = Student
    fields = ('id', 'name', 'scores')    

class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
  scores = ScoreSerializer(many=True, read_only=True)
  class Meta:
    model = Professor
    fields = ('id', 'name', 'scores')