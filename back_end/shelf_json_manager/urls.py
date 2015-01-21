from django.conf.urls import patterns, url

from shelf_json_manager import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<shelf_name>\w+)/$', views.get_json, name='json'),
)
