import os
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from uploaded_pdf.models import DocumentPdf, Page
from pdf2image import convert_from_path, convert_from_bytes
import PyPDF2
from PIL import Image as PILImage
from io import BytesIO
import pyocr
from pyocr.builders import TextBuilder
from django.conf import settings
from .tasks import count_page, save_pages, save_file_path
from PIL import Image


@receiver(pre_save, sender=DocumentPdf)
def pre_save_document_pdf(sender, instance, **kwargs):
    if not instance.title:
        instance.title = instance.file.name.split('/')[-1].split('.')[0]

    instance.slug = slugify(instance.title)
    with BytesIO(instance.file.read()) as file:
            reader = PyPDF2.PdfReader(file)
            instance.page_number = len(reader.pages)

@receiver(post_save, sender=DocumentPdf)
def save_images(sender, instance, created, **kwargs):
    if created:
        if settings.SAVE_FILE_PATH :
            save_file_path.delay(instance.id)
        else :
            save_pages.delay(instance.id)
        

