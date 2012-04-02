from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photoeditor.views.home', name='home'),
    # url(r'^photoeditor/', include('photoeditor.foo.urls')),
    url(r'^$', 'photoeditor.editor.views.home', name='home'),
    url(r'^featherposturl$', 'photoeditor.editor.views.post', name='post'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
