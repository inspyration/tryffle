from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
import os
from uuid import uuid4

def file_path(instance, filename):
    date = instance.date
    year = date.year
    month = date.month
    directory = os.path.join(settings.MEDIA_ROOT, 'uploads', str(year), str(month))
    if(not os.path.exists(directory)):
        os.makedirs(directory)
    _, ext = os.path.splitext(filename)
    return os.path.join(directory, f'{uuid4()}{ext}')

def page_path(instance, filename):
    directory = os.path.join(settings.MEDIA_ROOT, 'pages', str(instance.document.title))
    if(not os.path.exists(directory)):
        os.makedirs(directory)
    _, ext = os.path.splitext(filename)
    return os.path.join('pages', str(instance.document.title), f'{instance.number}{ext}')

# Create your models here.
class DocumentPdf(models.Model):
    title = models.fields.CharField(max_length=100, blank=True, null=True) #obligatoire, déduit du nom du fichier, modifiagle
    date = models.fields.DateField(blank=False, null=False) #obligatoire, saisie à la main
    file = models.FileField(upload_to=file_path) #obligatoire, uploadé à la création
    slug = models.SlugField(blank=True, null=True) #obligatoire, déduit du nom du fichier
    page_number = models.fields.IntegerField(validators=[MinValueValidator(0)], default=0) #obligatoire, déduit du fichier

class Page(models.Model):
    document = models.ForeignKey(DocumentPdf, null=False, on_delete=models.CASCADE) #suppression de la page si suppression du document
    number = models.fields.IntegerField(validators=[MinValueValidator(0)]) #à incrémenter de 1 à chaque page de document 
    image = models.ImageField(upload_to=page_path) #obligatoire
    text = models.fields.CharField(max_length=100000) #non obligatoire
    file_path = models.FilePathField(path='media/pages', null=True, blank=True)

