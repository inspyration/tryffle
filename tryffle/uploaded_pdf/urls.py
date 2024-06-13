from django.urls import path, include
from rest_framework.routers import DefaultRouter
from uploaded_pdf.views import DocumentPdfViewSet, PageViewSet, TrigramPageViewSet

router = DefaultRouter()
router.register(r'documents', DocumentPdfViewSet, basename='documents')
router.register(r'pages', PageViewSet, basename='pages')
router.register(r'trigramme_search', TrigramPageViewSet, basename='trigramme')

urlpatterns = [
    path('', include(router.urls)),
]