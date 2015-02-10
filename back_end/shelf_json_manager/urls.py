from django.conf.urls import patterns, url

from shelf_json_manager import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(
        r'^get_thumbnail/(?P<pdf_name_arg>\w+)/$',
        views.pdf_thumbnail, name='pdf_thumbnail'),
    url(r'^(?P<shelf_name>\w+)/$', views.get_json, name='json'),

)
