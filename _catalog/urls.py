from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^countries/$', countries),
    url(r'^$', index),
    url(r'^contact.html$', contact),
    url(r'^blog.html$', blog),
    url(r'^about.html$', about),
    url(r'^index.html$', index),
    ]