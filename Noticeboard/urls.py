from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^NoticeboardApp/', include('NoticeboardApp.urls')),
                       url(r'^$', RedirectView.as_view(url='NoticeboardApp')),
                       )

# Serve static files when debug false
if settings.ENVIRONMENT == 'LIVE':
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )