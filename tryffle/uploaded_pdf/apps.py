from django.apps import AppConfig

class Uploaded_pdfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uploaded_pdf'

    def ready(self):
        import uploaded_pdf.signal