# Create your views here.
from django.http import (HttpResponse)
from django.shortcuts import render_to_response
from agricolulz.scores.models import PlayerScore, Game

	
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
	context = {
		"request" : request,
	}
	return render_to_response("allgames.html", context)

def all_players(request):
	context = {
		"request" : request,
	}
	return render_to_response("allplayers.html", context)

