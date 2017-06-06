"""info services."""
from info.models import Article, News


def get_article_queryset():
    """Get article queryset."""
    queryset = Article.objects.all().order_by('-id')

    return queryset


def get_article_object(uid):
    """Get article object."""
    return Article.objects.get(uid=uid)


def get_news_queryset():
    """Get news queryset."""
    return News.objects.all().order_by('-id')
