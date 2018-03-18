from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login, login, logout


import views

urlpatterns = [
    url(r'^$', views.AppIndexView.as_view(), name='app_index'),
    url(r'^accounts/login/$', login, name='user_login'),
    url(r'^accounts/logout/$', logout, name='user_logout'),
    #url(r'^access/company/(?P<pk>[0-9a-f-]+)/$', views.LogoAccessCompanyUpdateView.as_view(), name='logo_access_edit_company'),

]

