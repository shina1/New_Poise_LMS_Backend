from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter


from .views import(
    ExamListViewSet
)
# router = DefaultRouter()

# urlpatterns = router.urls

urlpatterns = [
    url(r'^$', ExamListViewSet.as_view(), name='exam_view'),
]