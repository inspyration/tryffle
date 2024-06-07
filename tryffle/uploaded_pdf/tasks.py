from io import BytesIO
import os
from time import sleep
from celery import shared_task
from pdf2image import convert_from_path, convert_from_bytes
from uploaded_pdf.models import DocumentPdf, Page
import PyPDF2
from PIL import Image
import sys
import pyocr
from pyocr.builders import TextBuilder
from django.conf import settings



@shared_task
def process_pdf(pdf_path):
    print(f'ijeijijdiejdiejdiejdiejdiejfifuizxo,zoddozejdijdiehfuopenhnhhnvncxhudhrddruhruvhuhvuhfvuhvuhufhuvfhuvhfuvhfuvhuvhuvhfuv')
    sleep(10)  
    print(f'ijeijijdiejdiejdiejdiejdiejfifuizxoijeijijdiejdiejdiejdiejdiejfifuizxoijeijijdiejdiejdiejdiejdiejfifuizxoijeijijdiejdiejdiejdiejdiejfifuizxoijeijijdiejdiejdiejdiejdiejfifuizxo')
    return f'Processed {pdf_path}'


@shared_task
def count_page(id):
    instance = DocumentPdf.objects.get(pk=id)
    with BytesIO(instance.file.read()) as file:
            reader = PyPDF2.PdfReader(file)
            instance.page_number = len(reader.pages)

@shared_task
def save_pages(id):
    instance = DocumentPdf.objects.get(pk=id)
    with BytesIO(instance.file.read()) as file:
            images = convert_from_bytes(file.getvalue())
            for nb, image in enumerate(images):
                with BytesIO() as image_io:
                    image.save(image_io, format='PNG')
                    image_io.seek(0)
                    page = Page(document=instance, number=nb)
                    page.image.save(f"page_{nb:02}.png", image_io)
                    tools = pyocr.get_available_tools()
                    tool = tools[0]
                    lang = 'fra'
                    path = settings.MEDIA_ROOT + '/pages/' + str(instance.title) + '/' + str(nb) + '.png'
                    txt = tool.image_to_string(Image.open(path), lang=lang, builder=pyocr.builders.TextBuilder())
                    page.text = txt
                    page.save()

@shared_task
def save_file_path(id):
    instance = DocumentPdf.objects.get(pk=id)
    with BytesIO(instance.file.read()) as file:
            images = convert_from_bytes(file.getvalue())
            for nb, image in enumerate(images):
                with BytesIO() as image_io:
                    image.save(image_io, format='PNG')
                    image_io.seek(0)
                    page = Page(document=instance, number=nb)
                    directory = os.path.join(settings.MEDIA_ROOT, 'pages', str(instance.title))
                    if(not os.path.exists(directory)):
                        os.makedirs(directory)
                    image.save(directory + '/' + str(nb) + '.png')
                    tools = pyocr.get_available_tools()
                    tool = tools[0]
                    lang = 'fra'
                    path = settings.MEDIA_ROOT + '/pages/' + str(instance.title) + '/' + str(nb) + '.png'
                    txt = tool.image_to_string(Image.open(path), lang=lang, builder=pyocr.builders.TextBuilder())
                    page.file_path = os.path.join(directory, f'{nb}.png')
                    page.text = txt
                    page.save()

