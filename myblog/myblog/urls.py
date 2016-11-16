from django.conf.urls import (patterns, include, url)

# use Django server /media/ files
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^category/(?P<column_slug>[^/]+)/$', 'blog.views.category_detail',
        name='category'),
    url(r'^article/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$',
        'blog.views.article_detail', name='article'),
    url(r'^archives/$', 'blog.views.archives', name='archives'),
    url(r'^resources/$', 'blog.views.resources', name='resources'),
    url(r'^messages/$', 'blog.views.messages', name='messages'),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
