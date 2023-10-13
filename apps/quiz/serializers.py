from rest_framework import serializers

from apps.quiz.models import QuizCategory, Quiz, Question, Answer, UserQuiz
from django.contrib.auth import get_user_model

User = get_user_model()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id', 'question',
            'answer', 'is_true',
        )
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = (
            'id', 'quiz',
            'question', 'image',
            'answers',
        )

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = (
            'id', 'name',
            'quiz_category', 
            'questions',
        )

class QuizCategorySerializer(serializers.ModelSerializer):
    quizies = QuizSerializer(many=True, read_only=True)
    class Meta:
        model = QuizCategory
        fields = (
            'id', 'name',
            'image', 'quizies',
        )


class UserQuizSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    quiz_id = serializers.IntegerField()
    quiz_list = serializers.ListField()


    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        quiz_id = validated_data.get('quiz_id')
        quiz_list = validated_data.get('quiz_list')
        quiz = Quiz.objects.filter(pk=quiz_id).first()
        user_quiz = UserQuiz.objects.create(
            quiz=quiz,
            user=User.objects.filter(pk=user_id).first(),
            question_amount=quiz.questions.count()
        )
        for quiz in quiz_list:
            if Question.objects.filter(id=quiz['question_id']).first().answers.get(is_true=True).id == quiz['answer_id']:
                user_quiz.true_answer +=1
                user_quiz.save()
        return user_quiz
    

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.user.username,
            'quiz': instance.quiz.name,
            'true_answer': instance.true_answer,
            'question_amount': instance.question_amount
        }

#         {
#     "user_id": 1,
#     "quiz_id": 1,
#     "quiz_list": [
#         {
#             "question_id":1,
#             "answer_id":1
#         }
#     ]
# }