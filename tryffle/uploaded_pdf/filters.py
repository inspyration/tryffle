from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Value
from django.db.models.functions import Cast
from rest_framework import filters

class TrigramSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_query = request.query_params.get(self.search_param, '').strip()
        if search_query:
            queryset = queryset.annotate(
                similarity=TrigramSimilarity('text', search_query),
            ).filter(similarity__gt=0.95).order_by('-similarity')
        return queryset
