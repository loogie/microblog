from django.conf.urls import patterns, include, url

from . import views
from blog.views import PostListView, PostDetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^microblog/', include('microblog.foo.urls')),
    url(r'^$', views.HomepageView.as_view(), name="home"),
    url(r'^blog/$', PostListView.as_view(), name="blog_list"),
    url(r'^blog/(?P<pk>\d+)/$', PostDetailView.as_view(), name="blog_detail"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
