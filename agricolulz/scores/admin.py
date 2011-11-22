from scores.models import Player, Game, PlayerScore
from django.contrib import admin

class PlayerAdmin(admin.ModelAdmin):
  fieldsets = [
	(None,		{'fields' : ['name']}), 
	('Info',	{'fields' : ['email', 'date_joined']}),
  ]
  list_display = ('name', 'email', 'date_joined', 'number_of_games_played')

class PlayerScoreAdmin(admin.ModelAdmin):
  list_display = ('game_date', 'player_name', 'total_score')
  list_filter = ['player']

class PlayerInline(admin.TabularInline):
  model = PlayerScore
  extra = 5

class GameAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Game info', {'fields': ['deck', 'date']}),
  ]
  list_display = ('date', 'deck', 'number_of_players', 'game_winner')
  inlines = [PlayerInline]

admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerScore, PlayerScoreAdmin)
admin.site.register(Game, GameAdmin)

