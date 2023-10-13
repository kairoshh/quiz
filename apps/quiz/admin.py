from django.contrib import admin

from apps.quiz.models import QuizCategory, Question, Quiz, UserQuiz, Answer

admin.site.register(QuizCategory)
admin.site.register(UserQuiz)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)