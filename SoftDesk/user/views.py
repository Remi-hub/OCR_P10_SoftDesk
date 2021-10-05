from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from user.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import CustomUser
from rest_framework import status
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     user_data = self.request
    #
    #     new_user = CustomUser.objects.create_user(
    #         email=user_data['email'],
    #         first_name=user_data['first_name'],
    #         last_name=user_data['last_name'],
    #         username=user_data['username'],
    #         password=user_data['password']
    #     )
    #
    #     new_user.save()
    #
    #     serializer = UserSerializer(new_user)
    #     return Response(serializer.data)