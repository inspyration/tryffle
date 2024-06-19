#Mock(spec=django.core.files.File); mock_file.read.return_value = "fake file contents"
from django.test import TestCase, override_settings
from uploaded_pdf.models import DocumentPdf, Page
from unittest.mock import patch, MagicMock
from uploaded_pdf import signal
from uploaded_pdf.signal import pre_save_document_pdf, save_images
from django.db.models.signals import pre_save, post_save
from django.core.files import File
import tempfile
from pathlib import Path
from unittest import mock
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile

# Create your tests here.
class UploadedPdfTest(TestCase):

    def test_model(self):
    
        model = DocumentPdf(
            date=date(2024, 6, 18),
            file=ContentFile(b"jeijdeij", name="foo.pdf")
        )
        import pdb; pdb.set_trace()
        self.assertEqual(model.title, 'test')
        self.assertEqual(model.slug, 'test')
        self.assertEqual(model.page_number, 2)
        self.assertEqual(model.date, date(2024, 6, 18))
        self.assertEqual(model.file, mock_pdf_file)
        