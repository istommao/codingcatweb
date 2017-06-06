"""collector views."""
from django.views import generic

from collector.models import ResourceType, Resource


class CollectListView(generic.TemplateView):
    """Collect listview."""

    view_name = 'collect_list'

    template_name = 'collector/collectlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = ResourceType.objects.all()
        resources = Resource.objects.all()

        category_uid = self.request.GET.get('category')

        if category_uid:
            try:
                category = ResourceType.objects.get(uid=category_uid)
            except ResourceType.DoesNotExist:
                pass
            else:
                resources = resources.filter(category=category)
        else:
            resources = resources[:8]

        dataset = {
            'categories': categories,
            'resources': resources
        }
        context.update(dataset)
        return context
