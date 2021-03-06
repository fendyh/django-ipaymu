from django.conf import settings

try:
    from django.conf.urls import patterns, include, url
except:
    # Support for Django < 1.4
    from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('ipaymu.views',
    url(r'^ipaymu/process/$', 'process', name='ipaymu_process_url'),
    url(r'^ipaymu/notify/$', 'notify', name='ipaymu_notify_url'),
    url(r'^ipaymu/completed/$', 'return_page', name='ipaymu_return_url'),
    url(r'^ipaymu/canceled/$', 'cancel_page', name='ipaymu_cancel_url'),
)

# Ipaymu test page available only in Debug mode.
if settings.DEBUG:
    urlpatterns += patterns('ipaymu.views',
        url(r'^ipaymu/testpage/$', 'test_page', name='test_page'),
    )