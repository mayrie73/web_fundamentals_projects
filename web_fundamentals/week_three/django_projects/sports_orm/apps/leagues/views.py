from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		'baseball_leagues': League.objects.filter(sport='Baseball'),
		'womens_league': League.objects.filter(name__contains='Womens'),
		'hockey': League.objects.filter(name__contains='Hockey'),
		'not_football':League.objects.exclude(name__contains="Football"),
		'conferences': League.objects.filter(name__contains='conference'),
		'atlantic': League.objects.filter(name__contains='atlantic'),
		'dallas': Team.objects.filter(location='Dallas'),
		'raptors': Team.objects.filter(team_name__contains="raptors"),
		'city': Team.objects.filter(location__contains="city"),
		'begins_with_t': Team.objects.filter(team_name__startswith="t"),
		

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")