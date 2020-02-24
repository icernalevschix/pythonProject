import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(ObjectType):
    jobs = graphene.List(PostType)

    def resolve_jobs(self, info, **kwargs):
        return Post.objects.all()


schema = graphene.Schema(query=Query)
