from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from .views import *


urlpatterns = [
    url(r'^$', index),
    url(r'^region-uno/$', regionUno),
    url(r'^temperatura/$', tableTemperatura),
    url(r'^humedad/$', tableHumedad),
    url(r'^sonido/$', tableSonido),
    url(r'^co2/$', tableCO2),
    url(r'^chart/temperatura/$', chartTemperatura)
]

if settings.DEBUG :
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]