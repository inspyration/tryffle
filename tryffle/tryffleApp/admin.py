from django.contrib import admin
from tryffleApp.models import DocumentPdf, Page
# Register your models here.

class DocumentPdfAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

class PageAdmin(admin.ModelAdmin):
    list_display = ('document', 'number')

admin.site.register(DocumentPdf, DocumentPdfAdmin)
admin.site.register(Page, PageAdmin)