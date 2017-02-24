from django.conf.urls import url
from web1 import views as web1_views


urlpatterns = [
    url(r'list/(?P<block_id>\d+)', web1_views.article_list),
    url(r'create/(?P<block_id>\d+)', web1_views.article_create),
]