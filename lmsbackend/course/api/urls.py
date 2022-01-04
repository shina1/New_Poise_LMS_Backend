from django.urls import path
from django.conf.urls import url

from .views import (
    CourseListView, 
    CourseDetailsView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,

    CourseModuleListView,
    CourseModuleDetailsView,
    CourseModuleCreateView,
    CourseModuleUpdateView,
    CourseModuleDeleteView,

    CourseReviewListView,
    CourseReviewDetailsView,
    CourseReviewCreateView,
    CourseReviewUpdateView,
    CourseReviewDeleteView,

    CourseRegDetialView,
    CourseRegDetialDetView,
    CourseRegDetialDeleteView,
    )

urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='course_list'),
    url(r'^create/$',CourseCreateView.as_view(), name='create_course'),
    url(r'^(?P<pk>\d+)/$', CourseDetailsView.as_view(), name='course_detials'),
    url(r'^(?P<pk>\d+)/update/$', CourseUpdateView.as_view(), name='update_course'),
    url(r'^(?P<pk>\d+)/delete/$', CourseDeleteView.as_view(), name='delete_course'),
    # course modules url
    url(r'^(?P<course_pk>\d+)/module/$',CourseModuleListView.as_view(), name='module_list'),
    url(r'^(?P<course_pk>\d+)/module/create/$',CourseModuleCreateView.as_view(), name='module_create' ),
    url(r'^(?P<course_pk>\d+)/module/(?P<pk>\d+)/$',CourseModuleDetailsView.as_view(), name='module_details'),
    url(r'^(?P<course_pk>\d+)/module/(?P<pk>\d+)/update/$',CourseModuleUpdateView.as_view(), name='module_update'),
    url(r'^(?P<course_pk>\d+)/module/(?P<pk>\d+)/delete/$',CourseModuleDeleteView.as_view(), name='module_delete'),
    # course reviews url

    url(r'^(?P<course_pk>\d+)/review/$',CourseReviewListView.as_view(), name='review_list'),
    url(r'^(?P<course_pk>\d+)/review/create/$',CourseReviewCreateView.as_view(), name='review_create' ),
    url(r'^(?P<course_pk>\d+)/review/(?P<pk>\d+)/$',CourseReviewDetailsView.as_view(), name='review_details'),
    url(r'^(?P<course_pk>\d+)/review/(?P<pk>\d+)/edit/$',CourseReviewUpdateView.as_view(), name='review_update'),
    url(r'^(?P<course_pk>\d+)/review/(?P<pk>\d+)/delete/$',CourseReviewDeleteView.as_view(), name='review_delete'),

    # course enrolled users list view
    url(r'^(?P<course_pk>\d+)/enroll/$', CourseRegDetialView.as_view(), name='course_reg_user_list'),
    url(r'^(?P<course_pk>\d+)/enroll/(?P<pk>\d+)/$', CourseRegDetialDetView.as_view(), name='course_reg_user_detials'),
    url(r'^(?P<course_pk>\d+)/enroll/(?P<pk>\d+)/delete/$',CourseRegDetialDeleteView.as_view(),name='course_reg_user_delete')
]