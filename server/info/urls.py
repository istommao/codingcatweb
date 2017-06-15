"""info urls module."""
from extensions.utils import generate_urlpatterns

from info import views


URLS = [
    ('^column/(?P<column_uid>.+)/article/(?P<article_uid>.+)/$',
     views.ColumnArticleView),
    ('^column/$', views.ColumnListView),
    ('^column/(?P<uid>.+)/$', views.ColumnDetailView),
    ('^article/$', views.ArticleListView),
    ('^article/(?P<uid>.+)/$', views.ArticleDetailView),
]

# pylint: disable=C0103
urlpatterns = generate_urlpatterns(URLS)
