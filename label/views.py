from django.shortcuts import render
from django.views import generic
from .models import (
    Members, MusicBand, ConcertHall, MemberRoles, ConcertHallContract,
    ConcertHallManager, ConcertProgram, MemberToMusicBand, MusicBandContract
)
# Create your views here.

def index(request):

    return render(
        request,
        'index.html',
    )

def members(request):
    data = Members.objects.all()
    return render(request, 'members.html', {'data': data})

def music_bands(request):
    data = MusicBand.objects.all()
    return render(request, 'music_bands.html', {'data': data})

def concert_halls(request):
    data = ConcertHall.objects.all()
    return render(request, 'concert_halls.html', {'data': data})

def member_roles(request):
    data = MemberRoles.objects.all()
    return render(request, 'member_roles.html', {'data': data})

def concert_hall_contracts(request):
    data = ConcertHallContract.objects.all()
    return render(request, 'concert_hall_contracts.html', {'data': data})

def concert_hall_managers(request):
    data = ConcertHallManager.objects.all()
    return render(request, 'concert_hall_managers.html', {'data': data})

def concert_programs(request):
    data = ConcertProgram.objects.all()
    return render(request, 'concert_programs.html', {'data': data})

def member_to_music_bands(request):
    data = MemberToMusicBand.objects.all()
    return render(request, 'member_to_music_bands.html', {'data': data})

def music_band_contracts(request):
    data = MusicBandContract.objects.all()
    return render(request, 'music_band_contracts.html', {'data': data})