from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'agricolulz.main.views.index'),
    url(r'^login/', 'agricolulz.main.views.login'),
    url(r'^signup/', 'agricolulz.main.views.signup'),
    url(r'^players/', include('agricolulz.scores.player_urls')),
    url(r'^games/', include('agricolulz.scores.game_urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
