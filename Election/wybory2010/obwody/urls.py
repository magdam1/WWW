from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.first, name='first'),
    url(r'^([0-9]+)/$', views.second, name='second'),
    url(r'^([0-9]+)/([0-9]+)/$', views.third, name='third'),
    url(r'^([0-9]+)/([0-9]+)/([0-9]+)/$', views.fourth, name='fourth'),

    url(r'^edit/$', views.edit, name='edit'),
    url(r'^accept/$', views.accept, name='accept'),
]