"""server views."""
from django.views import generic

from info.services import get_article_queryset, get_news_queryset


class SilentNoteView(generic.TemplateView):
    """Silent note view."""

    view_name = 'note'
    template_name = 'note.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexView(generic.TemplateView):
    """Index view."""

    view_name = 'index'

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dataset = {
            'articles': get_article_queryset()[:5],
            'news': get_news_queryset()[:5]
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
