from django.db import models
from base.models import NewUser
from datetime import datetime

# Create your models here.

class Course(models.Model):
    title = models.CharField(unique=True, max_length=120,blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255,blank=False, default='')
    description = models.CharField(max_length=255,blank=True, default='')
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=125,blank=True, default='')
    course_run = models.BooleanField(default=False)
    course_start_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    course_end_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    paid = models.BooleanField(default=False)
    course_price =  models.CharField(max_length=125,blank=True,null=True, default='0')
    req_prequalification = models.BooleanField(default=False)
    req_final_exam = models.BooleanField(default=False)
    pre_cutoff = models.CharField(max_length=125,blank=True, default='')
    final_cutoff = models.CharField(max_length=125,blank=True, default='')
    attendance = models.CharField(max_length=125,blank=True, default='')
    certification = models.BooleanField(blank=True, default=False)
    url = models.URLField(unique=False,blank=True, default='')

    def __str__(self):
        return self.title
    
    @property
    def is_expired(self):
        if self.courseend_date == datetime.now:
            return True
        return False

class CourseModule(models.Model):
    title  = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, 
    related_name='coursemodule')

    class Meta:
        unique_together = ['course', 'order']
        ordering = ['order',]

        def __str__(self):
            return self.title

class CourseReview(models.Model):
    user = models.ForeignKey(NewUser, models.SET_NULL,
    blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, 
    related_name='coursereview')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        unique_together = ['email', 'course']

    def __str__(self):
        return '{0.rating} ratings by {0.full_name} for {0.course}'.format(self) 

class CourseRegDetial(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='courseregdetial')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True,null=True, related_name='courseregdetial')
    enrolment_date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    payment_made = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255)

    class Meta: 
        unique_together = ['user', 'course']

    def __str__(self):
        return str(self.course)
