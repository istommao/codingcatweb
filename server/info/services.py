"""info services."""
from info.models import Article


def get_article_queryset():
    """Get article queryset."""
    queryset = Article.objects.all()[:5]

    return queryset


def get_article_object(uid):
    """Get article object."""
    return Article.objects.get(uid=uid)
