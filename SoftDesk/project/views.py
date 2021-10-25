from rest_framework import viewsets
from project.serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from project.models import Project, Issue, Comment
from django.db.models import Q
from project.permissions import ProjectAndIsAuthenticated, IssueAndIsAuthenticated, CommentAndIsAuthenticated

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):

    permission_classes = [ProjectAndIsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(Q(author=self.request.user) |
                                      Q(contributors=self.request.user)).distinct()


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniqueProjectViewSet(viewsets.ModelViewSet):

    permission_classes = [ProjectAndIsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['pk'])


class IssueViewSet(viewsets.ModelViewSet):

    permission_classes = [IssueAndIsAuthenticated]
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        serializer.save(issue_author_user=self.request.user,
                        project_id=self.kwargs['project_pk'])


class CommentViewSet(viewsets.ModelViewSet):

    permission_classes = [CommentAndIsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issues=self.kwargs['issue_pk']).filter(
            Q(issues__project__contributors=self.request.user) |
            Q(issues__project__author=self.request.user)
            ).distinct()

    def perform_create(self, serializer):
        serializer.save(comment_author_user=self.request.user,
                        issues_id=self.kwargs['issue_pk'])


class UniqueCommentViewSet(viewsets.ModelViewSet):

    permission_classes = [CommentAndIsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(id=self.kwargs['pk']).filter(
            Q(issues__project__contributors=self.request.user) |
            Q(issues__project__author=self.request.user)
        ).distinct()
