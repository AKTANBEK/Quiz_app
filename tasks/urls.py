from django.urls import path
from .views import QuestionAPIView, QuestionListAPIView, answer_questions

urlpatterns = [
    path('quiz/<int:pk>/', QuestionAPIView.as_view()),
    path('otvet/', answer_questions),
    path('quiz/', QuestionListAPIView.as_view())
]
