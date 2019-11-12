from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from django.http import Http404

class ProfessorListView(generics.ListCreateAPIView):
  queryset = Professor.objects.all()
  serializer_class = ProfesorSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['id','name']

  def get_object(self):
    queryset = self.get_queryset()
    obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
    return obj

class ProfessorView(APIView):
  def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

  def get(self, request, pk, format=None):
      snippet = self.get_object(pk)
      serializer = ProfesorSerializer(snippet)
      return Response(serializer.data)

  def put(self, request, pk, format=None):
      snippet = self.get_object(pk)
      serializer = ProfesorSerializer(snippet, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      snippet = self.get_object(pk)
      snippet.delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 

class StudentListView(generics.ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['id','name']

  def get_object(self):
    queryset = self.get_queryset()
    obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
    return obj

class ScoreListView(generics.ListCreateAPIView):
  queryset = Score.objects.all()
  serializer_class = ScoreSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['id','name', 'student', 'professor','value']

  def get_object(self):
    queryset = self.get_queryset()
    obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
    return obj