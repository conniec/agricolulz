from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('agricolulz.scores.views',
    # Examples:
    url(r'^(\d+)$', 'player_details'),
    url(r'^$', 'all_players'),

)