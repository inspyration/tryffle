from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

def file_path():
    return 
# Create your models here.
class DocumentPdf(models.Model):
    title = models.fields.CharField(max_length=100) #obligatoire, déduit du nom du fichier, modifiagle
    date = models.fields.DateField() #obligatoire, saisie à la main
    file = models.FileField() #obligatoire, uploadé à la création
    slug = models.SlugField() #obligatoire, déduit du nom du fichier
    page_number = models.fields.IntegerField(validators=[MinValueValidator(0)]) #obligatoire, déduit du fichier

class Page(models.Model):
    document = models.ForeignKey(DocumentPdf, null=False, on_delete=models.CASCADE) #suppression de la page si suppression du document
    number = models.fields.IntegerField(validators=[MinValueValidator(0)]) #à incrémenter de 1 à chaque page de document 
    image = models.ImageField() #obligatoire
    text = models.fields.CharField(max_length=1000) #non obligatoire