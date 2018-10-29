from django_elasticsearch_dsl import DocType, Index
from .models import BlogPost


posts = Index('posts')


@posts.doc_type
class PostDocument(DocType):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'text']
