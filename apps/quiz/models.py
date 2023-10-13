from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class QuizCategory(models.Model):
    name = models.CharField(max_length=121, verbose_name='Название')
    image = models.ImageField(upload_to='quiz/images', verbose_name='Картинка')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class Quiz(models.Model):
    quiz_category = models.ForeignKey(
        QuizCategory, on_delete=models.CASCADE, related_name='quizies')
    name = models.CharField(max_length=123, verbose_name='Название')
    image = models.ImageField(upload_to='quiz/images', verbose_name='Картинка')

    def __str__(self) -> str:
        return f'{self.name} {self.quiz_category}'
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=200, verbose_name='Вопрос')
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return f'{self.question} {self.quiz}'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    

class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=200, verbose_name='Ответ')
    is_true = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.answer} {self.question}'
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    
class UserQuiz(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='quizies')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users')
    true_answer = models.PositiveIntegerField(default=0)
    question_amount = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.true_answer} {self.question_amount} {self.quiz}'
    
    class Meta:
        verbose_name = 'Тест пользователя'
        verbose_name_plural = 'Тесты пользователя'