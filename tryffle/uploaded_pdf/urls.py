from django.urls import path, include
from rest_framework.routers import DefaultRouter
from uploaded_pdf.views import DocumentPdfViewSet, PageViewSet

router = DefaultRouter()
router.register(r'documents', DocumentPdfViewSet)
router.register(r'pages', PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]