import graphene
from graphene_django import DjangoObjectType

from biblioteca.models import Reserva

class ReservaType(DjangoObjectType):
    class Meta:
        model = Reserva

class Query(graphene.ObjectType):
    Reserva = graphene.List(ReservaType)

    def resolve_Reserva(self, info, **kwargs):
        return Reserva.objects.all()

class CreateReserva(graphene.Mutation):
    id = graphene.Int()
    id_usuario = graphene.Int()
    id_coleccion = graphene.Int()
    fechaReserva = graphene.Date()
    estadoReserva = graphene.String()

    class Arguments:
        id_usuario = graphene.Int()
        id_coleccion = graphene.Int()
        fechaReserva = graphene.Date()
        estadoReserva = graphene.String()

    def mutate(self, info, id_usuario, id_coleccion, fechaReserva, estadoReserva):
        reserva = Reserva(id_usuario=id_usuario, id_coelccion=id_coleccion, fechaReserva=fechaReserva, estadoReserva=estadoReserva)
        reserva.save()

        return CreateReserva(
            id=reserva.id,
            id_usuario=reserva.id_usuario,
            id_coleccion=reserva.id_coleccion,
            fechaReserva=reserva.fechaReserva,
            estadoReserva=reserva.estadoReserva,
        )

class Mutation(graphene.ObjectType):
    create_reserva = CreateReserva.Field()