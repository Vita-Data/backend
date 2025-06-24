from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, LabTestReportViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'reports', LabTestReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
