from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from project.serializers import ProjectSerializer
from project.models import Project
from user.serializers import UserSerializer
from user.models import CustomUser

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

