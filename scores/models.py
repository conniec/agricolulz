from django.db import models
import logging

logger = logging.getLogger(__name__)

class Game(models.Model):
  deck = models.CharField(max_length=10)
  date = models.DateTimeField('date')

  def number_of_players(self):
    return self.playerscore_set.count()

  def game_winner(self):
	players = self.player_set.all()
	print "hello"
	scores = [player.total_score() for player in players]
	winner = max(scores)
	return winner.name



class Player(models.Model):
  name = models.CharField(max_length=20)
  date_joined = models.DateTimeField('date joined')
  email = models.CharField(max_length=20)

  def __unicode__(self):
	print "whee"
	return self.name

  def number_of_games_played(self):
	return self.playerscore_set.count()

class PlayerScore(models.Model):
  player = models.ForeignKey(Player)
  game = models.ForeignKey(Game)
  fields = models.IntegerField()
  pastures = models.IntegerField()
  grain = models.IntegerField()
  vegetables = models.IntegerField()
  sheep = models.IntegerField()
  wild_boar = models.IntegerField()
  cattle = models.IntegerField()
  unused_spaces = models.IntegerField()
  fenced_stables = models.IntegerField()
  clay_rooms = models.IntegerField()
  stone_rooms = models.IntegerField()
  family = models.IntegerField()
  card_points = models.IntegerField()
  bonus_points = models.IntegerField()

  def player_name(self):
	return self.player.name

  def game_date(self):
	return self.game.date

  def total_score(self):
	return self.fields+self.pastures+self.grain+self.vegetables+self.sheep+self.wild_boar \
			+self.cattle+self.unused_spaces+self.fenced_stables+self.clay_rooms+self.stone_rooms \
			+self.family+self.card_points+self.bonus_points
  
