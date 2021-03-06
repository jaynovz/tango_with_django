from django.conf.urls import patterns, include, url
from django.conf import settings
from rango import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin  # UNCOMMENT THIS LINE

admin.autodiscover()  # UNCOMMENT THIS LINE, TOO!

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^rango/', include('rango.urls')),
                       url(r'^admin/', include(admin.site.urls)),  # ADD THIS LINE
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^tango_with_django_project/', include('tango_with_django_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

