from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView


from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.quiz.serializers import QuizCategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, UserQuizSerializer
from apps.quiz.models import QuizCategory, Question, Quiz, Answer, UserQuiz


class QuizCategoryView(ModelViewSet):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    permission_classes = (IsAuthenticated,)
    

class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)


class QuizView(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = (
        'name',
    )
    filterset_fields = (
        'quiz_category__name',
    )



class AnswerView(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated,)


class UserQuizView(CreateAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer
    permission_classes = (IsAuthenticated,)



