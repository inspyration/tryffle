from rest_framework import serializers
from .models import DocumentPdf, Page

class DocumentPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentPdf
        fields = ['id', 'title', 'page_number']

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'document', 'number', 'text', 'file_path']
