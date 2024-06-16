import graphene
import query_optimizer.filter
from . import models
import query_optimizer as query_optimizer
import django_filters


class UsersFilter(query_optimizer.filter.FilterSet):
    order_by = django_filters.OrderingFilter(
        fields=(
            [
                field.name + "__id" if field.is_relation else field.name
                for field in models.Users._meta.fields
            ]
        )
    )

    class Meta:
        model = models.Users
        fields = {
            field.name + "__id" if field.is_relation else field.name: ["exact", "in"]
            for field in models.Users._meta.fields
        }
        exclude = ["privileges", "metadata"]


class UsersType(query_optimizer.DjangoObjectType):
    id = graphene.ID(source="pk", required=True)

    class Meta:
        model = models.Users
        interfaces = (graphene.relay.Node,)
        filterset_class = UsersFilter


class UsersQuery(graphene.ObjectType):
    Users = query_optimizer.DjangoConnectionField(UsersType)


class MangasFilter(query_optimizer.filter.FilterSet):
    order_by = django_filters.OrderingFilter(
        fields=(
            [
                field.name + "__id" if field.is_relation else field.name
                for field in models.Mangas._meta.fields
            ]
        )
    )

    class Meta:
        model = models.Mangas
        fields = {
            field.name + "__id" if field.is_relation else field.name: ["exact", "in"]
            for field in models.Mangas._meta.fields
        }
        exclude = ["privileges", "metadata"]


class MangasType(query_optimizer.DjangoObjectType):
    id = graphene.ID(source="pk", required=True)

    class Meta:
        model = models.Mangas
        interfaces = (graphene.relay.Node,)
        filterset_class = MangasFilter


class MangasQuery(graphene.ObjectType):
    Mangas = query_optimizer.DjangoConnectionField(MangasType)


class Query(UsersQuery, MangasQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
