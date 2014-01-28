from django.conf.urls import patterns, url
from mymarketingapp import views


urlpatterns = patterns('',
    url(r'^$', views.customer, name='customer'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^detail/$', views.detail, name='detail'))

