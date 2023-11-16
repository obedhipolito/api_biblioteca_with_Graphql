import graphene
from graphene_django import DjangoObjectType

from biblioteca.models import CatalogoEnLinea

class CatalogoType(DjangoObjectType):
    class Meta:
        model = CatalogoEnLinea
class Query(graphene.ObjectType):
    Catalogo = graphene.List(CatalogoType)

    def resolve_Catalogo(self, info, **kwargs):
        return CatalogoEnLinea.objects.all()

class CreateCatalogo(graphene.Mutation):
    id = graphene.Int()
    id_coleccion = graphene.Int()
    id_inventario = graphene.Int()
    enlace = graphene.String()

    class Arguments:
        id_coleccion = graphene.Int()
        id_inventario = graphene.Int()
        enlace = graphene.String()

    def mutate(self, info, id_coleccion, id_inventario, enlace):
        catalogo = CatalogoEnLinea(id_coleccion=id_coleccion, id_inventario=id_inventario, enlace=enlace)
        catalogo.save()

        return CreateCatalogo(
            id=catalogo.id,
            id_coleccion=catalogo.id_coleccion,
            id_inventario=catalogo.id_inventario,
            enlace=catalogo.enlace,
        )

class Mutation(graphene.ObjectType):
    create_catalogo = CreateCatalogo.Field()