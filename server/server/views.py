"""server views."""
from django.views import generic

from info.services import get_article_queryset


class IndexView(generic.TemplateView):
    """Index view."""

    view_name = 'index'

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dataset = {
            'articles': get_article_queryset()
        }
        context.update(dataset)
        return context


class AboutView(generic.TemplateView):
    """Index view."""

    view_name = 'about'

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
