from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^loans/$', views.loans_list, name='loans_list'),
    url(r'^client/(?P<client_id>\d+)/$', views.client_detail, name='client_detail'),
]
