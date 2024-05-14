from django.shortcuts import render
from django.views import generic
from .models import Members, MemberRoles, MemberToMusicBand, MusicBand, MusicBandContract, ConcertHallContract, ConcertHall, ConcertHallManager, ConcertProgram

# Create your views here.

def index(request):

    return render(
        request,
        'index.html',
    )