from django.db import models

class Game(models.Model):
  deck = models.CharField(max_length=10)
  date = models.DateTimeField('date')

class Player(models.Model):
  name = models.CharField(max_length=20)
  date_joined = models.DateTimeField('date joined')
  email = models.CharField(max_length=20)

#class PlayerScore(models.Model):
#  player = models
