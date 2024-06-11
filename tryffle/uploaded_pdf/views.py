from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .tasks import process_pdf
from django.conf import settings
from uploaded_pdf.models import DocumentPdf, Page
from inertia import render as inertia_render
from uploaded_pdf.serializers import DocumentPdfSerializer, PageSerializer
from rest_framework import viewsets

# Create your views here.
def documents(request):   
    document = DocumentPdf.objects.all()
    #return render(request, 'documents.html', {'documents':document})
    #documents = DocumentPdf.objects.values('id', 'title', 'page_number')
    serializer = DocumentPdfSerializer(document, many=True)
    return inertia_render(request, "Document", props={"documents": serializer.data})

def pages(request, id):
    document = DocumentPdf.objects.get(id=id)
    pages = Page.objects.filter(document=document)
    serializer = PageSerializer(pages, many=True)
    return inertia_render(request, "Pages", {"pages": serializer.data})
    #return render(request, 'pages.html', {'document': document})

def page_detail(request, document_id, id):
    document = get_object_or_404(DocumentPdf, pk=document_id)
    page = get_object_or_404(Page, document=document, number=id)
    serializer = PageSerializer(page, many=False)
    return inertia_render(request, "Page_Detail", props={"page": serializer.data})
    #return render(request, 'page-detail.html', {'page': page})

def test(request):
    #return inertia_render(request, 'index.html')
    return inertia_render(request, "Test", props={"name": "World"})

class DocumentPdfViewSet(viewsets.ModelViewSet):
    queryset = DocumentPdf.objects.all()
    serializer_class = DocumentPdfSerializer

