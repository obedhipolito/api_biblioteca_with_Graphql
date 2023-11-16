import graphene
from graphene_django import DjangoObjectType

from biblioteca.models import Inventario

class InventarioType(DjangoObjectType):
    class Meta:
        model = Inventario

class Query(graphene.ObjectType):
    Inventario = graphene.List(InventarioType)

    def resolve_Inventario(self, info, **kwargs):
        return Inventario.objects.all()
    
class CreateInventario(graphene.Mutation):
    id = graphene.Int()
    id_Coleccion = graphene.Int()
    cantidadDisponible = graphene.Int()
    cantidadTotal = graphene.Int()
    fechaDeAdquisicion = graphene.Date()

    class Arguments:
        id_Coleccion = graphene.Int()
        cantidadDisponible = graphene.Int()
        cantidadTotal = graphene.Int()
        fechaDeAdquisicion = graphene.Date()

    def mutate(self, info, id_Coleccion, cantidadDisponible, cantidadTotal, fechaDeAdquisicion):
        inventario = Inventario(id_Coleccion=id_Coleccion, cantidadDisponible=cantidadDisponible, cantidadTotal=cantidadTotal, fechaDeAdquisicion=fechaDeAdquisicion)
        inventario.save()

        return CreateInventario(
            id=inventario.id,
            id_Coleccion=inventario.id_Coleccion,
            cantidadDisponible=inventario.cantidadDisponible,
            cantidadTotal=inventario.cantidadTotal,
            fechaDeAdquisicion=inventario.fechaDeAdquisicion,
        )

class Mutation(graphene.ObjectType):
    create_inventario = CreateInventario.Field()