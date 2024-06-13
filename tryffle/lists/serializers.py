from rest_framework import serializers

from uploaded_pdf.models import Page


class SebSerializer(serializers.ModelSerializer):
    document_name = serializers.ReadOnlyField(source="document.title")
    page_number = serializers.ReadOnlyField(source="number")

    class Meta:
        model = Page
        fields = ("document_name", "page_number")
