from django.conf.urls import patterns, include, url
from django.contrib import admin
from users import views
urlpatterns = patterns('',
    
    url(r'^$', views.home,name ="home"),
    url(r'^signup/$', views.signup,name ="signup"),
    url(r'^login/$', views.login,name ="login"),
    url(r'^home/$', views.user_home,name ="user_home"),
    url(r'^logout/$', views.logout,name ="logout"),
    url(r'^set_pwd/(?P<code>\w+)$', views.set_pwd,name ="set_pwd"),
)