from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^session/addword$', views.addword),
url(r'^session/clearsession$', views.clear),
]   