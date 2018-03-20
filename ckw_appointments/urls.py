from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login, login, logout
from django.views.decorators.cache import cache_page
from django.views.i18n import javascript_catalog

import views
from api import rest

@cache_page(86400, key_prefix='js18n')
def cached_javascript_catalog(request, **kwargs):
    js_info_dict = {
        'domain': 'djangojs',
        'packages': (
            'ckw_appointments',
        ),
    }
    return javascript_catalog(request, **js_info_dict)


urlpatterns = [
    url(r'^$', views.AppIndexView.as_view(), name='app_index'),
    url(r'^accounts/login/$', login, name='user_login'),
    url(r'^accounts/logout/$', logout, name='user_logout'),
    url(r'^jsi18n/$', cached_javascript_catalog, name='javascript-catalog'),
    url(r'^apiv2/tasklog/', rest.CreateTaskLogEntryView.as_view(), name='apiv2_create_tasklog'),

]

