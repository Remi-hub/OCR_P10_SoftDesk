from django.contrib import admin
from project.models import Project, Issue, Comment
# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
