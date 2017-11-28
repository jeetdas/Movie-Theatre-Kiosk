from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<theater_id>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<theater_id>[0-9]+)/(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<theater_id>[0-9]+)/(?P<movie_id>[0-9]+)/buyTicket/$', views.confirmTicket, name='confirmTicket'),
]