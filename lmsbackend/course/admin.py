from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import Course, CourseModule,CourseReview, CourseRegDetial

class CourseModuleInline(admin.StackedInline):
    model = CourseModule

class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseModuleInline,]

admin.site.unregister(Group)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseModule)
admin.site.register(CourseReview)
admin.site.register(CourseRegDetial)