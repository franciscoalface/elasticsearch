from django.shortcuts import render
from project.core.search import PostDocument
from elasticsearch_dsl.query import Q


def search(request):
    q = request.GET.get('q')
    if q:
        posts = PostDocument.search().query(
            Q('match', title=q) |
            Q('match', text=q)
        )
    else:
        posts = ''

    return render(request, 'search.html', {'posts': posts})
