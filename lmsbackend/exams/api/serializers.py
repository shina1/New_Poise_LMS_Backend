from rest_framework import serializers
# from user.models import User
from base.models import NewUser

from exams.models import Exam,GradedExam, PreQualificationExam, Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    choice = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'chioces',
            'answer'
        )


class PreQualificationExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreQualificationExam
        fields = ('__all__')

class ExamSerializer(serializers.ModelSerializer):
    prequalificationexam = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    question = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Exam
        fields = (
            'id',
            'title',
            'created_by',
            'created_at',
            'category',
            'can_retake',
            'duration',
            'course',
            'prequalificationexam',
            'question',
        )
    def get_questions(self, obj):
        questions = QuestionSerializer(obj.questions.all(), many=True)
        return questions 
    
    def create(self, request):
        data = request.data
        print(data)