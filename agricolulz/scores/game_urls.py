from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('agricolulz.scores.views',
    # Examples:
    url(r'^(\d+)$', 'game_details'),
    url(r'^$', 'all_games'),
    url(r'^new/$', 'new_game'),

)