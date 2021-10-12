from django.db import models
# Create your models here.


TYPE_CHOICES = (('Backend', 'Backend'), ('Frontend', 'Frontend'), ('iOS', 'iOS'), ('Android', 'Android'))
PRIORITY = (('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'))
TAG = (('Bug', 'Bug'), ('Improvement', 'Improvement'), ('Task', 'Task'))
STATUS = (('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Finished', 'Finished'))
ROLE = (('Author', 'Author'), ('Contributor', 'Contributor'))


class Project(models.Model):

    def __str__(self):
        return f'{self.title}'

    title = models.CharField(max_length=120, blank=False)
    description = models.TextField(max_length=1500, blank=False)
    type = models.CharField(choices=TYPE_CHOICES, max_length=120, blank=False)
    author = models.ForeignKey('user.CustomUser', related_name='project_author', on_delete=models.CASCADE)
    contributors = models.ManyToManyField('user.CustomUser', related_name='project_contributors')


class Issue(models.Model):

    def __str__(self):
        return f'{self.title}, {self.issue_author_user}'

    title = models.CharField(max_length=120, blank=False)
    description = models.TextField(max_length=1500, blank=False)
    priority = models.CharField(choices=PRIORITY, blank=False, max_length=50)
    tag = models.CharField(choices=TAG, blank=False, max_length=50)
    status = models.CharField(choices=STATUS, blank=False, max_length=50)
    issue_author_user = models.ForeignKey('user.CustomUser', related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('project.Project', related_name='issues', on_delete=models.CASCADE)


class Comment(models.Model):

    issues = models.ForeignKey('project.Issue', related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(max_length=1500, blank=False)
    comment_author_user = models.ForeignKey('user.CustomUser', related_name='comment_author', on_delete=models.CASCADE)
