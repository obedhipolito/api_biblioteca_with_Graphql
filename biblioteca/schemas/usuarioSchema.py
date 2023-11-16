from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType

class UsuarioType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('id', 'correo', 'nombre', 'a_paterno', 'a_materno', 'tipoDeUsuario', 'ciudad', 'password')
    
class CreateUser(graphene.Mutation):
    user = graphene.Field(UsuarioType)

    class Arguments:
        correo = graphene.String(required=True)
        nombre = graphene.String(required=True)
        a_paterno = graphene.String(required=True)
        a_materno = graphene.String(required=True)
        tipoDeUsuario = graphene.String(required=True)
        ciudad = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, correo, nombre, a_paterno, a_materno, tipoDeUsuario, ciudad, password):
        usuario = get_user_model()(
            correo=correo,
            nombre=nombre,
            a_paterno=a_paterno,
            a_materno=a_materno,
            tipoDeUsuario=tipoDeUsuario,
            ciudad=ciudad,
            password=password
        )
        usuario.set_password(password)
        usuario.save()
        return CreateUser(usuario=usuario)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

class Query(graphene.ObjectType):
    UsuarioActivo = graphene.Field(UsuarioType)
    Usuario = graphene.List(UsuarioType)

    def resolve_usuario(self, info):
        return get_user_model().objects.all()
    
    def resolve_usuarioActivo(self, info):
        Usuario = info.context.user
        if Usuario.is_anonymous:
            raise Exception('no estas logueado')
        return Usuario