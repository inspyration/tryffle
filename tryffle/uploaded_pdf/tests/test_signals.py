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

# Create your tests here.
class UploadedPdfTest(TestCase):
    @classmethod
    def setUpTestData(self):
        import pdb; pdb.set_trace()
        super().setUpTestData()
        pdf_path = Path('.') / 'uploaded_pdf'/ 'tests'/ 'assets'/ 'test.pdf'
        with open(pdf_path, 'rb') as pdf_file:
            self.test_pdf = SimpleUploadedFile('test.pdf', pdf_file.read(), content_type='application/pdf')
        self.model = DocumentPdf(
            date=date(2024, 6, 18),
            file=self.test_pdf
        )

    @patch('uploaded_pdf.signal.pre_save_document_pdf')
    @patch('uploaded_pdf.signal.save_images', MagicMock())
    def test_pre_save_signal(self, pre_save_document_pdf_mock):
        self.model.save()
        pre_save_document_pdf_mock.assert_called_once(sender=DocumentPdf, instance=self.model, **{})

    @patch('uploaded_pdf.signal.pre_save_document_pdf', MagicMock())
    @patch('uploaded_pdf.signal.save_images', MagicMock())
    def test_pre_save_good(self):
        pre_save_document_pdf(sender=DocumentPdf, instance=self.model)
        self.assertEqual(self.model.title, 'test')
        self.assertEqual(self.model.slug, 'test')
        self.assertEqual(self.model.page_number, 2)
        self.assertEqual(self.model.date, date(2024, 6, 18))
        self.assertEqual(self.model.file, self.test_pdf)

    


