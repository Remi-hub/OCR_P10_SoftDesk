from rest_framework import viewsets
from rest_framework import permissions
from project.serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from project.models import Project, Issue, Comment
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from project.permissions import IsAuthenticatedAndAuthor, IsAuthenticatedAndContributor

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(Q(author=self.request.user) |
                                      Q(contributors=self.request.user))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IssueViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedAndAuthor, IsAuthenticatedAndContributor]
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        serializer.save(issue_author_user=self.request.user,
                        project_id=self.kwargs['project_pk'])


class CommentViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedAndAuthor, IsAuthenticatedAndContributor]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issues=self.kwargs['issue_pk'])

    def perform_create(self, serializer):
        serializer.save(comment_author_user=self.request.user,
                        issues_id=self.kwargs['issue_pk'])



