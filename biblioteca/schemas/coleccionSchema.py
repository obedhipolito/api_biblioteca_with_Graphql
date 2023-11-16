import graphene
from graphene_django import DjangoObjectType

from biblioteca.models import Coleccion

class ColeccionType(DjangoObjectType):
    class Meta:
        model = Coleccion

class Query(graphene.ObjectType):
    Coleccion = graphene.List(ColeccionType)

    def resolve_Coleccion(self, info, **kwargs):
        return Coleccion.objects.all()

class CreateColeccion(graphene.Mutation):
    id = graphene.Int()
    id_Autor = graphene.Int()
    titulo = graphene.String()
    isbn = graphene.Int()
    tipoDeColeccion = graphene.String()
    descripcion = graphene.String()
    fechaPublicacion = graphene.String()
    categoria = graphene.String()
    estado = graphene.String()
    ubicacioEnBiblioteca = graphene.String()
    precio = graphene.Float()
    

    class Arguments:
        id_Autor = graphene.Int()
        titulo = graphene.String()
        isbn = graphene.Int()
        tipoDeColeccion = graphene.String()
        descripcion = graphene.String()
        fechaPublicacion = graphene.String()
        categoria = graphene.String()
        estado = graphene.String()
        ubicacioEnBiblioteca = graphene.String()
        descripcion = graphene.String()
        precio = graphene.Float()

    def mutate(self, info, id_Autor, titulo, isbn, tipoDeColeccion, descripcion, fechaPublicacion, categoria, estado, ubicacioEnBiblioteca, precio):
        coleccion = Coleccion(id_Autor=id_Autor, titulo=titulo, isbn=isbn, tipoDeColeccion=tipoDeColeccion, descripcion=descripcion, fechaPublicacion=fechaPublicacion, categoria=categoria, estado=estado, ubicacioEnBiblioteca=ubicacioEnBiblioteca, precio=precio)
        coleccion.save()

        return CreateColeccion(
            id=coleccion.id,
            id_Autor=coleccion.id_Autor,
            titulo=coleccion.titulo,
            isbn=coleccion.isbn,
            tipoDeColeccion=coleccion.tipoDeColeccion,
            descripcion=coleccion.descripcion,
            fechaPublicacion=coleccion.fechaPublicacion,
            categoria=coleccion.categoria,
            estado=coleccion.estado,
            ubicacioEnBiblioteca=coleccion.ubicacioEnBiblioteca,
            precio=coleccion.precio,
        )

class Mutation(graphene.ObjectType):
    create_coleccion = CreateColeccion.Field()