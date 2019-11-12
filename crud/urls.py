from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework.authtoken import views

urlpatterns = [
    url('api/v1/', include('school.urls')),
    url('admin/', admin.site.urls)
]

urlpatterns += [
    url('api/v1/', include('rest_framework.urls', namespace='rest_framework')),    
]
