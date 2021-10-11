from rest_framework import serializers
from project.models import Project, Issue, Comment
from user.serializers import UserSerializer
from user.models import CustomUser


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'contributors']
        extra_kwargs = {
            'contributors': {'allow_empty': True, 'required': False},
            'title': {'allow_null': True, 'required': False},
            'description': {'allow_null': True, 'required': False},
            'type': {'allow_null': True, 'required': False},
        }


class IssueSerializer(serializers.ModelSerializer):

    issue_author_username = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['issue_author_username', 'title', 'description', 'priority', 'tag',
                  'status', 'issue_author_user', 'created_at']

        extra_kwargs = {
            'issue_author_user': {'read_only': True},
            'title': {'allow_null': True, 'required': False},
            'description': {'allow_null': True, 'required': False},
            'priority': {'allow_null': True, 'required': False},
            'tag': {'allow_null': True, 'required': False},
            'status': {'allow_null': True, 'required': False},
        }

    def get_issue_author_username(self, obj):
        return obj.issue_author_user.username


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'issues', 'description', 'comment_author_user']

        extra_kwargs = {
            'comment_author_user': {'read_only': True},
            'issues': {'read_only': True}
        }
