# Create your views here.
from django.http import (HttpResponse)
from django.shortcuts import render_to_response
from agricolulz.scores.models import PlayerScore, Game, User

	
def game_details(game_id, request):
	game = Game.objects.get(pk=1)
	all_scores = PlayerScore.objects.filter(game__pk=1)
	all_fields = PlayerScore._meta.get_all_field_names()
	context = {
		"request" : request,
		"game" : game,
		"all_scores" : all_scores,
		"all_fields" : all_fields
	}
	return render_to_response("graph.html", context)

def all_games(request):
	all_games = Game.objects.all()
	context = {
		"request" : request,
		"all" : all_games,
		"type" : "games",
	}
	return render_to_response("all.html", context)

def all_players(request):
	all_players = User.objects.all()
	context = {
		"request" : request,
		"all" : all_players,
		"type" : "players",
	}
	return render_to_response("all.html", context)

