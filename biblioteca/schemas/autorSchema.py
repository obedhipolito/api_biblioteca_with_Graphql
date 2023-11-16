import graphene
from graphene_django import DjangoObjectType

from biblioteca.models import Autor

class AutorType(DjangoObjectType):
    class Meta:
        model = Autor

class Query(graphene.ObjectType):
    Autor = graphene.List(AutorType)

    def resolve_Autor(self, info, **kwargs):
        return Autor.objects.all()

class CreateAutor(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    a_paterno = graphene.String()
    a_materno = graphene.String()
    fechaNacimiento = graphene.Date()
    nacionalidad = graphene.String()
    biografia = graphene.String()

    class Arguments:
        nombre = graphene.String()
        a_paterno = graphene.String()
        a_materno = graphene.String()
        fechaNacimiento = graphene.Date()
        nacionalidad = graphene.String()
        biografia = graphene.String()

    def mutate(self, info, nombre, a_paterno, a_materno, fechaNacimiento, nacionalidad, biografia):
        autor = Autor(nombre=nombre, a_paterno=a_paterno, a_materno=a_materno, fechaNacimiento=fechaNacimiento, nacionalidad=nacionalidad, biografia=biografia)
        autor.save()

        return CreateAutor(
            id=autor.id,
            nombre=autor.nombre,
            a_paterno=autor.a_paterno,
            a_materno=autor.a_materno,
            fechaNacimiento=autor.fechaNacimiento,
            nacionalidad=autor.nacionalidad,
            biografia=autor.biografia,
        )

class Mutation(graphene.ObjectType):
    create_autor = CreateAutor.Field()