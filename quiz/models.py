from django.db import models


class Quiz(models.Model):
    quiz_title = models.CharField(max_length=50)
    quiz_description = models.CharField(max_length=100)
    quiz_difficulty = models.IntegerField()

class Question(models.Model):
    question_title = models.CharField(max_length=50)
    question_text = models.CharField(max_length=100)
    is_multi_answer = models.BooleanField()
    quiz_foreign_key = models.ForeignKey(Quiz, on_delete = models.CASCADE)

class Answer(models.Model):
    answer_title = models.CharField(max_length=50)
    answer_text = models.CharField(max_length=100)
    is_correct_answer = models.BooleanField()
    question_foreign_key = models.ForeignKey(Quiz, on_delete = models.CASCADE)



# Create your models here.
