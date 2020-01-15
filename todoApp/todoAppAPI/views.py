from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TaskSerializers, UserSerializers
from .models import Task
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_create')
    serializer_class = TaskSerializers

    # filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    # filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)

    filter_fields = ('completed',) # category task by attribute `completed`
    ordering = ('-date_create',) # sorting by date_create
    search_fields = ('task_name', 'task_desc',) # search for each column of db

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers

# # Task not complete, in due 
# class DueTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_create').filter(completed=False)
#     serializer_class = TaskSerializers

# class CompletedTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_create').filter(completed=True)
#     serializer_class = TaskSerializers
