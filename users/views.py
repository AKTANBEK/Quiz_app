from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from users.models import User
from users.serializers import RegisterUserSerializer, UserProfileSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        password = serializer.validated_data.pop('password2')

        User.objects.create(
            email=user_data['email'],
            password=make_password(password)
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)


