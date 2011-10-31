from django.db import models

class Game(models.Model):
  deck = models.CharField(max_length=10)
  date = models.DateTimeField('date')

class Player(models.Model):
  name = models.CharField(max_length=20)
  date_joined = models.DateTimeField('date joined')
  email = models.CharField(max_length=20)

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
  
  
