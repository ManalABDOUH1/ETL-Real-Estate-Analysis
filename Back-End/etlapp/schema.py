import graphene
from graphene_django import DjangoObjectType
from .models import * 
class LocationType(DjangoObjectType):
    class Meta: 
        model = Location
        fields = (
    'id' ,
    'Title' ,
    'Location',
    'Price',
    'Caracteristiques' ,
    'Pieces'  ,
    'Description' ,
    'Pictures' ,
    'Telephone',
    'Duree' ,
    'Surface',
        )  
class VenteType(DjangoObjectType):
    class Meta: 
        model = Vente
        fields = (
    'id' ,
    'Title' ,
    'Location',
    'Price',
    'Caracteristiques' ,
    'Pieces'  ,
    'Description' ,
    'Pictures' ,
    'Telephone',
    'Surface',
        )  
class Query(graphene.ObjectType):
    locations = graphene.List(LocationType)
    ventes = graphene.List(VenteType)


    def resolve_locations(root, info, **kwargs):
        # Querying a list
        return Location.objects.all()

    def resolve_ventes(root, info, **kwargs):
        # Querying a list
        return Vente.objects.all()
schema = graphene.Schema(query=Query)