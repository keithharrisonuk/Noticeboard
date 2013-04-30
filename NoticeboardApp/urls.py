from django.conf.urls.defaults import *

urlpatterns = patterns('NoticeboardApp.views',
                       url(r'^$', 'index'),
                       )
