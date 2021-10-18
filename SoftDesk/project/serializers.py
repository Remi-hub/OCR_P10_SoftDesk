from rest_framework import serializers
from project.models import Project, Issue, Comment


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
    issue_id = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['issue_id', 'issue_author_username', 'issue_author_user', 'title', 'description', 'priority', 'tag',
                  'status', 'created_at']

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

    def get_issue_id(self, obj):
        return obj.id


class CommentSerializer(serializers.ModelSerializer):

    comment_author_user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'issues', 'description', 'comment_author_user', 'comment_author_user']

        extra_kwargs = {
            'comment_author_user': {'read_only': True},
            'issues': {'read_only': True}
        }

    def get_comment_author_user(self, obj):
        return obj.comment_author_user.username
