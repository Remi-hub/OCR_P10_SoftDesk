from rest_framework import permissions
from project.models import Project, Issue, Comment


class IsAuthenticatedAndAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if isinstance(obj, Project):
            if obj.author == request.user:
                return True

        if isinstance(obj, Issue):
            if obj.issue_author_user == request.user:
                return True

        if isinstance(obj, Comment):
            if obj.comment_author_user == request.user:
                return True

        return False


class IsAuthenticatedAndContributor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if isinstance(obj, Project):
            if obj.contributors == request.user:
                return True

        if isinstance(obj, Issue):
            if obj.issue_author_user == request.user:
                return True

        if isinstance(obj, Comment):
            if obj.comment_author_user == request.user:
                return True

        return False


class ProjectAndIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if obj.author == request.user:
            return True

        if obj.contributors == request.user:
            return True

        return False


class IssueAndIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if obj.issue_author_user == request.user:
            return True

        return False


class CommentAndIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if obj.comment_author_user == request.user:
            return True

        return False
