from django.conf.urls import url

from app import views as app_views
urlpatterns = [
    url(r'^index/',app_views.get_all,name='index'),
    url(r'^get_one_xingshi/(?P<xingshi_id>\d+)',app_views.get_one_xingshi,name='get_one_xingshi'),
    url(r'^get_one_info/(?P<xingming_id>\d+)',app_views.get_one_info,name='get_one_info'),
    url(r'^add_one_xingming',app_views.add_one_xingming,name='add_one_xingming')
]