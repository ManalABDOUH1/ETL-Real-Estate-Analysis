from .models import Location
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *


class NewsDocumentSerializer(DocumentSerializer):
    class Meta :
        model = Location
        document = NewsDocument

        fields = ('Title', 'Location ')

        def get_location(self , obj):
            try :
                return obj.location.to_dict()
            except :
                return {}