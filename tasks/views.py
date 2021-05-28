from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question, AllAnswers
from .serializers import (
    QuestionSerializer, AnswerSerializer
)


class QuestionAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# class UserAnswerAPIView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated,]
#     http_method_names = ['POST',]
#
#     def create(self, request, *args, **kwargs):
#         user = request.user
#         post_data = request.data
#         print(post_data)
#         question = (post_data.get('questions')[0])
#         question_id = Question.objects.get(question=question).id
#
#         answers_data = post_data.get('answers')[0]
#         # answer = AllAnswers.objects.get(answer=answers_data).id
#
#         answer_serializer = AnswerPostSerializer(data=answers_data)
#         answer_serializer.is_valid(raise_exception=True)
#         print(answer_serializer.data)
#         serializer_data = {"questions": [question_id], "answers": [answers_data]}
#
#
#         return Response('questions answered', status=status.HTTP_201_CREATED)
#     # queryset = Question.objects.all()
#     # serializer_class = QuestionIsCorrectSerializer
#     # user_value = 0
#     # if queryset[0].question_is_correct != False:
#     #     user_value += 1
#     # else:
#     #     user_value += 0
#     # print(user_value)

@api_view(["POST"])
def answer_questions(request):
    data = request.data
    user = request.user
    dict_data = dict(data).items()

    if user.completed_test:
        return Response('dont cheat', status=status.HTTP_403_FORBIDDEN)
    else:
        for item in dict_data:
            question = item[0]
            answer = item[1][0]

            q = Question.objects.get(question=question)
            a = AllAnswers.objects.get(answer=answer)

            if a.question_id != q:
                return Response('something is wrong', status=status.HTTP_400_BAD_REQUEST)

            if a.is_correct:
                user.score += 1
                user.save()

        user.completed_test = True
        user.save()

    return Response('answered questions', status=status.HTTP_202_ACCEPTED)


class AnswerAPIView(generics.RetrieveAPIView):
    queryset = AllAnswers.objects.all()
    serializer_class = AnswerSerializer


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)
