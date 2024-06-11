from django.urls import path, include
from rest_framework.routers import DefaultRouter
from uploaded_pdf.views import DocumentPdfViewSet

router = DefaultRouter()
router.register(r'documents', DocumentPdfViewSet)

urlpatterns = [
    path('', include(router.urls)),
]