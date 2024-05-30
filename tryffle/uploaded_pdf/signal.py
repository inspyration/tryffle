from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from uploaded_pdf.models import DocumentPdf
import PyPDF2
from io import BytesIO

def count_pdf_pages(pdf_content):
    with BytesIO(pdf_content) as file:
        reader = PyPDF2.PdfFileReader(file)
        return reader.getNumPages()



@receiver(pre_save, sender=DocumentPdf)
def pre_save_document_pdf(sender, instance, **kwargs):
    if not instance.title:
        instance.title = instance.file.name.split('/')[-1].split('.')[0]

    instance.slug = slugify(instance.title)
    with BytesIO(instance.file.read()) as file:
            reader = PyPDF2.PdfReader(file)
            instance.page_number = len(reader.pages)