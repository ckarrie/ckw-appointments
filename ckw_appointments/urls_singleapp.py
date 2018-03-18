from django.conf.urls import url, include
from django.contrib import admin
from urls import urlpatterns

admin.autodiscover()

urlpatterns += [
    url(r'^db/', include(admin.site.urls)),
]
