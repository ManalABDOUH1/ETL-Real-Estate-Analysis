from django.shortcuts import render
#     ElasticSearch
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend ,
    CompoundSearchFilterBackend,
)
from .documents import *
from .serializers import *
# Create your views here.

class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer

    filter_backends = [
        FilteringFilterBackend ,
        CompoundSearchFilterBackend,
    ]

    search_fields = ('Title','Location')
    multi_match_search_fields = ('Title','Location')
    filter_fields = {
        'Title' : 'Title',
        'Location' : 'Location'
    }