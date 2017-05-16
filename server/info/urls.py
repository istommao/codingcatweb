"""info urls module."""
from extensions.utils import generate_urlpatterns

from info import views


URLS = [
    ('^article/$', views.ArticleListView),
    ('^article/(?P<uid>.+)/$', views.ArticleDetailView),
]

# pylint: disable=C0103
urlpatterns = generate_urlpatterns(URLS)
