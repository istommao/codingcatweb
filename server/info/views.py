"""info views."""
from django.views import generic

from info.services import (get_article_queryset, get_article_object,
                           get_column_object,
                           get_columns_queryset, get_articles_by_column)


class ColumnArticleView(generic.TemplateView):
    """Column article view"""

    view_name = 'column_article'
    template_name = 'info/column_article.html'

    def get_context_data(self, column_uid, article_uid, **kwargs):
        context = super().get_context_data(**kwargs)

        column = get_column_object(column_uid)
        articles = get_articles_by_column(column_uid)
        article = get_article_object(article_uid)

        dataset = {
            'column': column,
            'articles': articles,
            'article': article
        }
        context.update(dataset)
        return context


class ColumnDetailView(generic.TemplateView):
    """Column detail view"""

    view_name = 'column_detail'
    template_name = 'info/columndetail.html'

    def get_context_data(self, uid, **kwargs):
        context = super().get_context_data(**kwargs)

        column = get_column_object(uid)
        articles = get_articles_by_column(uid)

        dataset = {
            'column': column,
            'articles': articles
        }
        context.update(dataset)
        return context


class ColumnListView(generic.TemplateView):
    """Column list view"""

    view_name = 'column_list'
    template_name = 'info/columnlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dataset = {
            'columns': get_columns_queryset()
        }
        context.update(dataset)
        return context


class ArticleListView(generic.TemplateView):
    """Article list view."""

    view_name = 'article_list'

    template_name = 'info/articlelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dataset = {
            'articles': get_article_queryset()
        }
        context.update(dataset)
        return context


class ArticleDetailView(generic.TemplateView):
    """Article detail view."""

    view_name = 'article_detail'

    template_name = 'info/articledetail.html'

    def get_context_data(self, uid, **kwargs):
        context = super().get_context_data(**kwargs)

        dataset = {
            'article': get_article_object(uid)
        }
        context.update(dataset)
        return context
