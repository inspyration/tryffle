from inertia import render as inertia_render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from uploaded_pdf.models import Page
from .serializers import SebSerializer


def basic_list(request):
    return inertia_render(request, "Basic_List", props={})


def real_list(request):
    return inertia_render(request, "Real_List", props={})


class SebViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.select_related("document").all()
    serializer_class = SebSerializer


@api_view(['GET'])
def data_source(request):
        pages = Page.objects.select_related("document").all()
        serializer = SebSerializer(pages, many=True)
        return Response({"data": serializer.data})
