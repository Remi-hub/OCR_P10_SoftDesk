from rest_framework import serializers
from project.models import Project, Issue, Comment
from user.models import CustomUser


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author', 'contributors']

