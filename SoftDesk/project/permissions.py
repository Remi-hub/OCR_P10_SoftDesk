from rest_framework import permissions
from project.models import Project


class ProjectAndIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if obj.author == request.user:
            return True

        if request.method == 'GET':
            if request.user in obj.contributors.all():
                return True

        return False


class IssueAndIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            requested_project = Project.objects.get(id=view.kwargs['project_pk'])
        except Project.DoesNotExist:
            return False

        if request.user == requested_project.author:
            return True

        if request.user in requested_project.contributors.all():
            return True

        return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if obj.issue_author_user == request.user:
            return True

        return False


class CommentAndIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            requested_project = Project.objects.get(id=view.kwargs['project_pk'])
        except Project.DoesNotExist:
            return False

        if request.user == requested_project.author:
            return True

        if request.user in requested_project.contributors.all():
            return True

        return False

    def has_object_permission(self, request, view, obj):
        try:
            requested_project = Project.objects.get(id=view.kwargs['project_pk'])
        except Project.DoesNotExist:
            return False

        if request.user.is_superuser:
            return True

        if request.user == obj.comment_author_user:
            return True

        if request.method == 'GET':
            if request.user in requested_project.contributors.all():
                return True

        return False



