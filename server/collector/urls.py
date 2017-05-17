"""collector urls module."""
from extensions.utils import generate_urlpatterns

from collector import views


URLS = [
    ('^collector/$', views.CollectListView),
]

# pylint: disable=C0103
urlpatterns = generate_urlpatterns(URLS)
