"""info services."""
from info.models import Article, News, Column


def get_column_object(uid):
    """Get column object."""
    try:
        obj = Column.objects.get(uid=uid)
    except Column.DoesNotExist:
        obj = None
    return obj


def get_articles_by_column(uid):
    """Get_articles_by_column."""
    queryset = Article.objects.filter(
        column__uid=uid
    ).order_by('id')

    return queryset


def get_columns_queryset():
    """Get_columns_queryset."""
    queryset = Column.objects.all().only('uid', 'name').order_by('-id')

    return queryset


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
