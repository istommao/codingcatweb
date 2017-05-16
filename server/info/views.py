"""info views."""
from django.views import generic

from info.services import get_article_queryset, get_article_object


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
