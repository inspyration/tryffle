from rest_framework import serializers
from .models import DocumentPdf, Page

class DocumentPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentPdf
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    document = DocumentPdfSerializer(read_only=True)
    class Meta:
        model = Page
        fields = '__all__'
