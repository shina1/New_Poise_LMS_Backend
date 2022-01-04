from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/user/', include('base.api.urls', namespace='users')),
    path('api/v1/course/', include('course.api.urls')),
        path('api/v1/exam/', include('exams.api.urls')),
    path('api/v1/pre-exam/', include('exams.api.pre-exams.urls')),
    path('api/v1/final-exam/', include('exams.api.final-exam.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)