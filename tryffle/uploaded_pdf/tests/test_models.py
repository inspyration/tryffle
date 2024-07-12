from datetime import date
from pathlib import Path

from factory.django import mute_signals
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save, post_save
from django.test import TestCase, override_settings

from uploaded_pdf.models import DocumentPdf, Page

class UploadedPdfTest(TestCase):

    @mute_signals(pre_save, post_save)
    def test_model_without_signals(self):
        model = DocumentPdf(
            date=date(2024, 6, 18),
            title="title",
            slug="slug",
            file=ContentFile(b"truc", name="foo.pdf")
        )
        model.save()

        self.assertEqual(model.title, 'title')
        self.assertEqual(model.slug, 'slug')
        self.assertEqual(model.date, date(2024, 6, 18))
        self.assertTrue(model.file.path.startswith("/app/media/uploads"))
        self.assertEqual(model.file.read(), b'truc')
        self.assertEqual(model.page_number, 0)

    def test_model_nominal(self):
        with open(Path(".") / "uploaded_pdf" / "tests" / "assets" / "test.pdf", "rb") as f:
            pdf_content = f.read()
        model = DocumentPdf(
            date=date(2024, 6, 18),
            file=ContentFile(pdf_content, name="test.pdf"),
        )
        model.save()

        self.assertEqual(model.title, 'test')
        self.assertEqual(model.slug, 'test')
        self.assertEqual(model.date, date(2024, 6, 18))
        self.assertTrue(model.file.path.startswith("/app/media/uploads"))
        self.assertEqual(model.file.read(), pdf_content)
        self.assertEqual(model.page_number, 2)
