from django.contrib import admin
from uploaded_pdf.models import DocumentPdf, Page
# Register your models here.

class DocumentPdfAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('document', 'number')

admin.site.register(DocumentPdf, DocumentPdfAdmin)
admin.site.register(Page, PageAdmin)