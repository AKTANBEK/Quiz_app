from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.models import User
from tasks.models import Question


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            return serializers.ValidationError(
                {"Password: password fields don't match"}
            )
        return attrs


class UserQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']


class UserProfileSerializer(serializers.ModelSerializer):
    questions = UserQuestionSerializer(many=True)

    class Meta:
        model = User
        fields = ['email', 'questions', 'score']
