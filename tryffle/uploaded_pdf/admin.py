from django.contrib import admin
from uploaded_pdf.models import DocumentPdf, Page
# Register your models here.

class DocumentPdfAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'page_number')
    readonly_fields = ('page_number', 'title', 'slug',)
    search_fields = ('title',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('document', 'number', 'file_path')
    readonly_fields = ('file_path',)

admin.site.register(DocumentPdf, DocumentPdfAdmin)
admin.site.register(Page, PageAdmin)

