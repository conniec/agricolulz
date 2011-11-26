from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.forms import ModelForm
import logging

class Game(models.Model):
    deck = models.CharField(max_length=10)
    date = models.DateTimeField('date')

    def number_of_players(self):
        return self.playerscore_set.count()

    def game_winner(self):
        # player_scores = self.playerscore_set.all()
        # winner = ""
        # maxscore = 0
        # for each_player in player_scores:
        #     if each_player.total_score() > maxscore:
        #         maxscore = each_player.total_score()
        #         winner = each_player.player
        # return winner.username
        players = self.player_set.all()
        scores = [(player.total_score(), player.player) for player in players]
        maxScore, winner = max(scores)
        return winner.username

class PlayerUser(User):
    #user = models.OneToOneField(User)
    fav_animal = models.CharField(max_length=50, default='Sheep')
    objects = UserManager()
    # def __unicode__(self):
    #     return self.user

class UserForm(ModelForm):
    class Meta:
        model = User

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, created = UserProfile.objects.get_or_create(user=instance)
    
#post_save.connect(create_user_profile, sender=User)

class PlayerScore(models.Model):
    player = models.ForeignKey(PlayerUser)
    game = models.ForeignKey(Game)
    fields = models.IntegerField()
    pastures = models.IntegerField()
    grain = models.IntegerField()
    vegetables = models.IntegerField()
    sheep = models.IntegerField()
    wild_boar = models.IntegerField()
    cattle = models.IntegerField()
    unused_spaces = models.IntegerField(verbose_name="Unused Spaces")
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
  