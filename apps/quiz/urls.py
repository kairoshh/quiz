from apps.quiz.views import QuizCategoryView, QuestionView, QuizView, UserQuizView, AnswerView
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)


router = DefaultRouter()
router.register('quiz_category', QuizCategoryView),
router.register('quiz', QuizView)
urlpatterns = [
    path('token',  TokenObtainPairView.as_view()),
    path('user/', UserQuizView.as_view())
]

urlpatterns += router.urls
