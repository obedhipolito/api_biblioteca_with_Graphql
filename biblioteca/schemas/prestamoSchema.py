import graphene
from graphene_django import DjangoObjectType

from biblioteca.models import Prestamo

class PrestamoType(DjangoObjectType):
    class Meta:
        model = Prestamo

class Query(graphene.ObjectType):
    Prestamo = graphene.List(PrestamoType)

    def resolve_Prestamo(self, info, **kwargs):
        return Prestamo.objects.all()

class CreatePrestamo(graphene.Mutation):
    id = graphene.Int()
    id_usuario = graphene.Int()
    id_coleccion = graphene.Int()
    fechaInicio = graphene.Date()
    fechaVencimiento = graphene.Date()
    fechaDevolucion = graphene.Date()
    estadoPrestamo = graphene.String()


    class Arguments:
        id_usuario = graphene.Int()
        id_coleccion = graphene.Int()
        fechaInicio = graphene.Date()
        fechaVencimiento = graphene.Date()
        fechaDevolucion = graphene.Date()
        estadoPrestamo = graphene.String()

    def mutate(self, info, id_usuario, id_coleccion, fechaInicio, fechaVencimiento, fechaDevolucion, estadoPrestamo):
        prestamo = Prestamo(id_usuario=id_usuario, id_coleccion=id_coleccion, fechaInicio=fechaInicio, fechaVencimiento=fechaVencimiento, fechaDevolucion=fechaDevolucion, estadoPrestamo=estadoPrestamo)
        prestamo.save()

        return CreatePrestamo(
            id=prestamo.id,
            id_usuario=prestamo.id_usuario,
            id_coleccion=prestamo.id_coleccion,
            fechaInicio=prestamo.fechaInicio,
            fechaVencimiento=prestamo.fechaVencimiento,
            fechaDevolucion=prestamo.fechaDevolucion,
            estadoPrestamo=prestamo.estadoPrestamo,
        )

class Mutation(graphene.ObjectType):
    create_prestamo = CreatePrestamo.Field()