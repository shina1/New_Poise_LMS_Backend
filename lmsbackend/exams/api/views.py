from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
      HTTP_201_CREATED,
      HTTP_400_BAD_REQUEST
)
from rest_framework.generics import (
      ListAPIView,
      RetrieveAPIView,
      CreateAPIView,
      UpdateAPIView,
      DestroyAPIView,
      )

from exams.models import Exam
from exams.api.serializers import ExamSerializer

class ExamListViewSet(ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamViewSet(viewsets.ModelViewSet):
      queryset = Exam.objects.all()
      serializer_class = ExamSerializer

      def createExam(self, response):
            serializer = ExamSerializer(data=request.data)
            if serializer.is_valid():
                  exam = serializer.create(request)
                  if exam:
                        return Response(status=HTTP_201_CREATED)
            return Response(status=HTTP_400_BAD_REQUEST)