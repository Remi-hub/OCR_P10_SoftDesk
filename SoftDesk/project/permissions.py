from rest_framework import permissions


class IsAuthenticatedAndAuthor(permissions.BasePermission):


    def has_permission(self, request, view):
        pass

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if type(obj).__name__ == 'Project':
            if obj.author == request.user:
                return True

        if type(obj).__name__ == 'Issue':
            if obj.issue_author_user == request.user:
                return True

        if type(obj).__name__ == 'Comment':
            if obj.comment_author_user == request.user:
                return True

        return False


class IsAuthenticatedAndContributor(permissions.BasePermission):

    def has_permission(self, request, view):
        pass

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if type(obj).__name__ == 'Project':
            if obj.contributors == request.user:
                return True

        if type(obj).__name__ == 'Issue':
            if obj.issue_author_user == request.user:
                return True

        if type(obj).__name__ == 'Comment':
            if obj.comment_author_user == request.user:
                return True

        return False


class ProjectAndIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if type(obj).__name__ == 'Project':
            if obj.author == request.user:
                return True

        if type(obj).__name__ == 'Project':
            if obj.contributors == request.user:
                return True


class IssueAndIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj.issue_author_user == request.user.id:
            return True


class CommentAndIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj.comment_author_user == request.user.id:
            return True







#TODO check les permissions