from django.db.models import Avg
from rest_framework import serializers

from course.models import Course, CourseModule,CourseReview,CourseRegDetial


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email' : {'write_only': True}
        }
        model = CourseReview
        fields = ('__all__')

    def validate_rating(self, value):
        if value in range(1,6):
               return value
        raise serializers.ValidationError(
                'Rating must be between 1 and 5'
            )  

class CourseModuleSerializer(serializers.ModelSerializer):
    description = serializers.CharField(allow_null=True, default='')
    content = serializers.CharField(allow_null=True, default='')
    class Meta:
        extra_kwargs = {
            'order' : {'write_only': True}
        }
        model = CourseModule
        fields = ('__all__')

class CourseRegDetialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegDetial
        fields = ('__all__')

class CourseSirializer(serializers.ModelSerializer):
    coursemodule = serializers.PrimaryKeyRelatedField(many=True, read_only=True,)
    
    coursereview = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    courseregdetial = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    is_expired = serializers.ReadOnlyField()
    average_rating = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", input_formats=['%d-%m-%Y',])
    course_start_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", input_formats=['%d-%m-%Y',])
    course_end_date =  serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", input_formats=['%d-%m-%Y',])
    description = serializers.CharField(allow_null=True, default=None)

    class Meta:
        model = Course
        fields = (
        'id',
        'title',
        'created_at',
        'created_by',
        'description',
        'image',
        'category',
        'course_run',
        'course_start_date',
        'course_end_date',
        'coursemodule',
        'courseregdetial',
        'paid',
        'course_price',
        'req_prequalification',
        'req_final_exam',
        'pre_cutoff',
        'final_cutoff',
        'attendance',
        'coursereview',
        'average_rating',
        'is_expired',
        'url'
        )
    
    def get_average_rating(self, obj):
        average = obj.coursereview.aggregate(Avg('rating')).get('rating__avg')

        if average is None:
           return 0 
        return round(average*2) / 2   