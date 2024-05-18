from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import (
    Members, MusicBand, ConcertHall, MemberRoles, ConcertHallContract,
    ConcertHallManager, ConcertProgram, MemberToMusicBand, MusicBandContract
)
from .forms import MemberForm
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

def edit_member(request, members_id):
    member = get_object_or_404(Members, members_id=members_id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit_member.html', {'form': form})

def create_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm()
    return render(request, 'create_member.html', {'form': form})

def delete_member(request, members_id):
    member = get_object_or_404(Members, members_id=members_id)
    if request.method == "POST":
        member.delete()
        return redirect('members')
    return redirect('members')
