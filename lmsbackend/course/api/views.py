from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissions
# REST_FRAMEWORK VIEWSETS
from rest_framework.generics import (
      ListAPIView,
      RetrieveAPIView,
      CreateAPIView,
      UpdateAPIView,
      DestroyAPIView,
      )

from course import models
from course.models import Course, CourseModule, CourseReview, CourseRegDetial
from .serializers import CourseSirializer, CourseModuleSerializer, CourseReviewSerializer, CourseRegDetialSerializer
# Create your views here.

# course model view serializer
class CourseListView(ListAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = Course.objects.all()
    serializer_class = CourseSirializer

class CourseDetailsView(RetrieveAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = Course.objects.all()
    serializer_class = CourseSirializer

class CourseCreateView(CreateAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = Course.objects.all()
    serializer_class = CourseSirializer

class CourseUpdateView(UpdateAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = Course.objects.all()
    serializer_class = CourseSirializer

class CourseDeleteView(DestroyAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = Course.objects.all()
    serializer_class = CourseSirializer


# course module view serializer

class CourseModuleListView(ListAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer
    allow_empty = False

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

class CourseModuleDetailsView(RetrieveAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

class CourseModuleCreateView(CreateAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer

    def perform_create(self,serializer):
        course = get_object_or_404(
            models.Course, pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)    

class CourseModuleUpdateView(UpdateAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            course_id=self.kwargs.get('course_pk'),
            pk=self.kwargs.get('pk')
        )

class CourseModuleDeleteView(DestroyAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer

# get_queryset get multiple items while get_object gets a single item.

# course review view set
class CourseReviewListView(ListAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

class CourseReviewDetailsView(RetrieveAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

class CourseReviewCreateView(CreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer

    def perform_create(self,serializer):
        course = get_object_or_404(
            models.Course, pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)    

class CourseReviewUpdateView(UpdateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            course_id=self.kwargs.get('course_pk'),
            pk=self.kwargs.get('pk')
        )

class CourseReviewDeleteView(DestroyAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer

# view users taking a course

class CourseRegDetialView(ListAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = CourseRegDetial.objects.all()
    serializer_class = CourseRegDetialSerializer 

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
    


class CourseRegDetialDetView(RetrieveAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = CourseRegDetial.objects.all()
    serializer_class = CourseRegDetialSerializer 

class CourseRegDetialDeleteView(DestroyAPIView):
    permission_classes = [DjangoModelPermissions,]
    queryset = CourseRegDetial.objects.all()
    serializer_class = CourseRegDetialSerializer