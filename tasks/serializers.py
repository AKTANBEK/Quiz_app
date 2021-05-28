from rest_framework import serializers

from tasks.models import Question, AllAnswers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllAnswers
        fields = ['answer', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['questions', 'answers']
