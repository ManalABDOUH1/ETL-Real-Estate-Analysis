from django_elasticsearch_dsl import ( Document ,  fields , Index )
from .models import Location

PUBLISHER_INDEX=Index('location')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas =1
)
@PUBLISHER_INDEX.doc_type

class NewsDocument (Document):
    id=fields.IntegerField(attr="id")
    Title=fields.TextField(
        fields={
            "raw" : {
                "type":'keyword'
            }
        }
    )       
    Location=fields.TextField(
        fields={
            "raw" : {
                "type":'keyword'
            }
        }
    ) 

    class Django(object):
        model = Location