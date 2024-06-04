from django.shortcuts import render
from django.http import HttpResponse
from .tasks import process_pdf

# Create your views here.
def home(request):
    pdf_path = "/path/to/your/pdf_file.pdf"
    
    result = process_pdf.delay(pdf_path)
    return HttpResponse('<h1>Test</h1>')