from datetime import date
from pathlib import Path
import pytest
from rest_framework.exceptions import ValidationError
from factory.django import mute_signals
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save, post_save
from django.test import TestCase, override_settings

from uploaded_pdf.models import DocumentPdf, Page
from uploaded_pdf.serializers import DocumentPdfSerializer, PageSerializer

from PIL import Image
import io

class UploadedPdfTest(TestCase):


    def valid_test_serializer(self):
        valid_data = {
            'title' : 'Test Document',
            'date' : date(2024, 6, 18),
            'file' : ContentFile(b"truc", name="foo.pdf"),
            'slug' : 'test-document',
            'page_number' : '2'
        }
        serializer = DocumentPdfSerializer(data=valid_data)
        assert serializer.is_valid()
        assert serializer.validated_data['title'] == 'Test Document'
        assert serializer.validated_data['date'] == date(2024, 6, 18)
        assert serializer.validated_data['file'].name == 'foo.pdf'
        assert serializer.validated_data['slug'] == 'test-document'
        assert serializer.validated_data['page_number'] == 2


    def invalid_test_serializer(self):
        invalid_data = {
        'title': 'Titre du document',
        'date': date.today(),
        'file': ContentFile(b"truc", name="foo.pdf"),
        'slug': 'titre-du-document',
        'page_number': -1
        }
        serializer = DocumentPdfSerializer(data=invalid_data)
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
        invalid_data = {
            'title': 'Titre du document',
            'file': ContentFile(b"truc", name="foo.pdf"),
            'slug': 'titre-du-document',
            'page_number': 5
        }
        serializer = DocumentPdfSerializer(data=invalid_data)
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)

