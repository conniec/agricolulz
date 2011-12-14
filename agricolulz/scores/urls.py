from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('agricolulz.scores.views',
    # Examples:
    url(r'^(\d+)$', 'game_details'),
    url(r'^games/$', 'all_games'),
    url(r'^games/new$', 'new_game'),

)
