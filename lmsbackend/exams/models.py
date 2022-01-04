from django.db import models

# Create your models here.
from base.models import NewUser
from course.models import Course

# Create your models here.


class Exam(models.Model):
    # exam categories
    STANDALONE = 1
    PRETEST = 2
    FINAL = 3

    CAT_CHOICES = ( 
        (STANDALONE, 'Standalone_Exam'),
        (PRETEST, 'prequalification_Test'),
        (FINAL, 'Final')
    )

    title = models.CharField(max_length=155)
    created_by = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='exam')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.PositiveSmallIntegerField(choices=CAT_CHOICES, blank=False, null=False, default=1)
    can_retake = models.BooleanField(default=False)
    duration = models.DurationField(blank=True, null=True, default=0)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True, related_name='exam')

    def __str__(self):
        return str(self.title)

class GradedExam(models.Model):
    student = models.ForeignKey(NewUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='gradedexam') # that took the exam
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, blank=True, null=True, related_name='gradedexam') #the exam taken
    grade = models.FloatField() #the students score after taking the exam
    passed = models.BooleanField(default=False) 

    def __str__(self):
        return str(self.student.username)

# model for course pre-qualification exam
class PreQualificationExam(models.Model):
    student = models.ForeignKey(NewUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='prequalificationexam') # that took the exam
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, blank=True, null=True, related_name='prequalificationexam') #the exam taken
    grade = models.FloatField() #the students score after taking the exam
    passed = models.BooleanField(default=False) 

    def __str__(self):
        return str(self.student.username)

# model for course final exam
class FinalExam(models.Model):
    student = models.ForeignKey(NewUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='finalexam') # that took the exam
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, blank=True, null=True, related_name='finalexam') #the exam taken
    grade = models.FloatField() #the students score after taking the exam
    passed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.student.username)

# model for standalone exams
class StandaloneExam(models.Model):
    student = models.ForeignKey(NewUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='standaloneexam') # that took the exam
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, blank=True, null=True, related_name='standaloneexam') #the exam taken
    grade = models.FloatField() #the students score after taking the exam
    passed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.student.username) 


class Choice(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    question = models.TextField()
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answer')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='question')
    order = models.SmallIntegerField()

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return str(self.question)