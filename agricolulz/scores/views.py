# Create your views here.
from django.http import (HttpResponse)
from django.shortcuts import render_to_response
from agricolulz.scores.models import PlayerScore, Game

def index(request):
	print "yoyo"
	return HttpResponse("hi")
	
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
