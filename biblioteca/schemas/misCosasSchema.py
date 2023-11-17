import graphene
from graphene_django import DjangoObjectType
from biblioteca.models import misCosas

class MisCosasType(DjangoObjectType):
    class Meta:
        model = misCosas

class Query(graphene.ObjectType):
    MisCosas = graphene.List(MisCosasType)

    def resolve_MisCosas(self, info, **kwargs):
        return misCosas.objects.all()
    
class CreateMisCosas(graphene.Mutation):
    id=graphene.Int()
    id_usuario=graphene.Int()
    id_coleccion=graphene.Int()
    fechaAdquisicion=graphene.Date()

    class Arguments:
        id_usuario=graphene.Int()
        id_coleccion=graphene.Int()
        fechaAdquisicion=graphene.Date()

    def mutate(self, info, id_usuario, id_coleccion, fechaAdquisicion):
        miscosas = misCosas(id_usuario=id_usuario, id_coleccion=id_coleccion, fechaAdquisicion=fechaAdquisicion)
        miscosas.save()

        return CreateMisCosas(
            id=miscosas.id,
            id_usuario=miscosas.id_usuario,
            id_coleccion=miscosas.id_coleccion,
            fechaAdquisicion=miscosas.fechaAdquisicion,
        )

class Mutation(graphene.ObjectType):
    create_miscosas = CreateMisCosas.Field()