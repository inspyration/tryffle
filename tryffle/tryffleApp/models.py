from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class DocumentPdf(models.Model):
    title = models.fields.CharField(max_length=100)
    date = models.fields.DateField()
    file = models.FileField()
    slug = models.SlugField()
    page_number = models.fields.IntegerField(validators=[MinValueValidator(0)])

class Page(models.Model):
    document = models.ForeignKey(DocumentPdf, null=False, on_delete=models.CASCADE)
    number = models.fields.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField()
    text = models.fields.CharField(required=False)