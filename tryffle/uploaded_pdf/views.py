from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .tasks import process_pdf
from django.conf import settings
from uploaded_pdf.models import DocumentPdf, Page
from inertia import render as inertia_render
# Create your views here.
def documents(request):   
    document = DocumentPdf.objects.all()
    return render(request, 'documents.html', {'documents':document})

def pages(request, id):
    document = DocumentPdf.objects.get(id=id)
    return render(request, 'pages.html', {'document': document})

def page_detail(request, document_id, id):
    document = get_object_or_404(DocumentPdf, pk=document_id)
    page = get_object_or_404(Page, document=document, number=id)
    return render(request, 'page-detail.html', {'page': page})

def test(request):
    #return inertia_render(request, 'index.html')
    return inertia_render(request, "Test", props={"name": "World"})
