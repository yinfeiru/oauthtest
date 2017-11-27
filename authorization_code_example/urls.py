from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^oauth_credentials$', views.oauth_credentials),
    url(r'^authenticate$', views.authenticate),
    url(r'^refresh_token$', views.refresh_token),
    url(r'^test_webhook$', views.test_webhook),
]
