"""info views."""
from django.views import generic


class ArticleListView(generic.TemplateView):
    """Article list view."""

    view_name = 'article_list'

    template_name = 'info/articlelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
