from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/$', views.SearchAPIView.as_view(), name='search'),
    url(r'^loans/$', views.LoansListAPIView.as_view(), name='loans'),
    url(r'^client/(?P<pk>\d+)/$', views.ClientDetailAPIView.as_view(), name='client'),
]
