from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/top5$', views.post_top5),
    url(r'^post/new/$', views.new_post, name='new_post'),
    ]