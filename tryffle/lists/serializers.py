from django.template.defaultfilters import linebreaksbr
from rest_framework import serializers

from uploaded_pdf.models import Page


class SebSerializer(serializers.ModelSerializer):
    document_name = serializers.ReadOnlyField(source="document.title")
    page_number = serializers.ReadOnlyField(source="number")
    text = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Page
        fields = ("document_name", "page_number", "text")

    def get_text(self, obj):
        return linebreaksbr(obj.text)
