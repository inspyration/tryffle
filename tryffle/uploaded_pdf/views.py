from django.shortcuts import render
from django.http import HttpResponse
from .tasks import process_pdf
from django.conf import settings
from uploaded_pdf.models import DocumentPdf, Page

# Create your views here.
def home(request):   
    document = DocumentPdf.objects.all()
    return render(request, 'documents.html', {'documents':document})

def pages(request, id):
    document = DocumentPdf.objects.get(id=id)
    pages = document.page_set.all()
    return render(request, 'pages.html', {'document': document, 'pages': pages})

def page_detail(request, id):

    page = Page.objects.get(id=id)
    return render(request, 'page-detail.html', {'page': page})