from scores.models import User, Game, PlayerScore, PlayerUser
from django.contrib import admin

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

admin.site.register(PlayerUser)
admin.site.register(PlayerScore, PlayerScoreAdmin)
admin.site.register(Game, GameAdmin)

