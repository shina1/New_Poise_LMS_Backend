from django.contrib import admin

from .models import Exam, PreQualificationExam,FinalExam,StandaloneExam,Choice, Question
# Register your models here.


class QuestionInline(admin.StackedInline):
    model = Question

class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInline,]

admin.site.register(Exam, ExamAdmin)
admin.site.register(PreQualificationExam)
admin.site.register(FinalExam)
admin.site.register(StandaloneExam)
admin.site.register(Choice)
admin.site.register(Question)
