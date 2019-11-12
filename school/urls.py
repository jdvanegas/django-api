from rest_framework.urlpatterns import format_suffix_patterns
from school.api_views import *
from django.urls import path

urlpatterns = [
  path('professors/', ProfessorListView.as_view(), name='professors'),
  path('professors/<int:pk>/', ProfessorView.as_view()),
  path('students/', StudentListView.as_view(), name='students'),
  path('scores/', ScoreListView.as_view(), name='scores')
]

urlpatterns = format_suffix_patterns(urlpatterns)