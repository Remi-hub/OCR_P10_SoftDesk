"""SoftDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from user.views import RegisterView
from rest_framework_nested import routers
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views

from project.views import ProjectViewSet, UniqueProjectViewSet,IssueViewSet, CommentViewSet
from user.views import CreateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'project', UniqueProjectViewSet, basename='project')

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'issues', IssueViewSet, basename='issues')

issues_router = routers.NestedSimpleRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.LoginView.as_view(), name='login'),
    path(r'', include(router.urls)),
    path(r'', include(projects_router.urls)),
    path(r'', include(issues_router.urls))
]
