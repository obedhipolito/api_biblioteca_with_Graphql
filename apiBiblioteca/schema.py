import graphene
import graphql_jwt


import biblioteca.schemas.autorSchema
import biblioteca.schemas.usuarioSchema
import biblioteca.schemas.prestamoSchema
import biblioteca.schemas.reservaSchema
import biblioteca.schemas.coleccionSchema
import biblioteca.schemas.inventarioSchema
import biblioteca.schemas.catalogoSchema


class Query(biblioteca.schemas.autorSchema.Query,
            biblioteca.schemas.usuarioSchema.Query,
            biblioteca.schemas.prestamoSchema.Query,
            biblioteca.schemas.reservaSchema.Query,
            biblioteca.schemas.coleccionSchema.Query,
            biblioteca.schemas.inventarioSchema.Query,
            biblioteca.schemas.catalogoSchema.Query,
            graphene.ObjectType):
    pass

class Mutation(biblioteca.schemas.autorSchema.Mutation,
                biblioteca.schemas.usuarioSchema.Mutation,
                biblioteca.schemas.prestamoSchema.Mutation,
                biblioteca.schemas.reservaSchema.Mutation,
                biblioteca.schemas.coleccionSchema.Mutation,
                biblioteca.schemas.inventarioSchema.Mutation,
                biblioteca.schemas.catalogoSchema.Mutation,
                graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)