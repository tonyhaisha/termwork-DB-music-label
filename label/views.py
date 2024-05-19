from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import (
    Members, MusicBand, ConcertHall, MemberRoles, ConcertHallContract,
    ConcertHallManager, ConcertProgram, MemberToMusicBand, MusicBandContract
)
from .forms import (
    MemberForm, MusicBandForm, ConcertHallForm, MemberRolesForm, ConcertHallContractForm,
    ConcertHallManagerForm, ConcertProgramForm, MemberToMusicBandForm, MusicBandContractForm
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

def edit_concert_hall_contract(request, concert_hall_contract_id):
    concert_hall_contracts = get_object_or_404(ConcertHallContract, concert_hall_contract_id=concert_hall_contract_id)
    if request.method == "POST":
        form = ConcertHallContractForm(request.POST, instance=concert_hall_contracts)
        if form.is_valid():
            form.save()
            return redirect('concert_hall_contracts')
    else:
        form = ConcertHallContractForm(instance=concert_hall_contracts)
    return render(request, 'edit_concert_hall_contract.html', {'form': form})

def create_concert_hall_contract(request):
    if request.method == "POST":
        form = ConcertHallContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_hall_contracts')
    else:
        form = ConcertHallContractForm()
    return render(request, 'create_concert_hall_contract.html', {'form': form})

def delete_concert_hall_contract(request, concert_hall_contract_id):
    concert_hall_contracts = get_object_or_404(ConcertHallContract, concert_hall_contract_id=concert_hall_contract_id)
    if request.method == "POST":
        concert_hall_contracts.delete()
        return redirect('concert_hall_contracts')
    return redirect('concert_hall_contracts')

def edit_concert_hall_manager(request, concert_hall_manager_id):
    concert_hall_managers = get_object_or_404(ConcertHallManager, concert_hall_manager_id=concert_hall_manager_id)
    if request.method == "POST":
        form = ConcertHallManagerForm(request.POST, instance=concert_hall_managers)
        if form.is_valid():
            form.save()
            return redirect('concert_hall_managers')
    else:
        form = ConcertHallManagerForm(instance=concert_hall_managers)
    return render(request, 'edit_concert_hall_manager.html', {'form': form})

def create_concert_hall_manager(request):
    if request.method == "POST":
        form = ConcertHallManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_hall_managers')
    else:
        form = ConcertHallManagerForm()
    return render(request, 'create_concert_hall_manager.html', {'form': form})

def delete_concert_hall_manager(request, concert_hall_manager_id):
    concert_hall_managers = get_object_or_404(ConcertHallManager, concert_hall_manager_id=concert_hall_manager_id)
    if request.method == "POST":
        concert_hall_managers.delete()
        return redirect('concert_hall_managers')
    return redirect('concert_hall_managers')

def edit_concert_hall(request, concert_hall_id):
    concert_hall = get_object_or_404(ConcertHall, concert_hall_id=concert_hall_id)
    if request.method == "POST":
        form = ConcertHallForm(request.POST, instance=concert_hall)
        if form.is_valid():
            form.save()
            return redirect('concert_halls')
    else:
        form = ConcertHallForm(instance=concert_hall)
    return render(request, 'edit_concert_hall.html', {'form': form})

def create_concert_hall(request):
    if request.method == "POST":
        form = ConcertHallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_halls')
    else:
        form = ConcertHallForm()
    return render(request, 'create_concert_hall.html', {'form': form})

def delete_concert_hall(request, concert_hall_id):
    concert_hall = get_object_or_404(ConcertHall, concert_hall_id=concert_hall_id)
    if request.method == "POST":
        concert_hall.delete()
        return redirect('concert_halls')
    return redirect('concert_halls')

def edit_concert_program(request, concert_program_id):
    concert_program = get_object_or_404(ConcertProgram, concert_program_id=concert_program_id)
    if request.method == "POST":
        form = ConcertProgramForm(request.POST, instance=concert_program)
        if form.is_valid():
            form.save()
            return redirect('concert_programs')
    else:
        form = ConcertProgramForm(instance=concert_program)
    return render(request, 'edit_concert_program.html', {'form': form})

def create_concert_program(request):
    if request.method == "POST":
        form = ConcertProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_programs')
    else:
        form = ConcertProgramForm()
    return render(request, 'create_concert_program.html', {'form': form})

def delete_concert_program(request, concert_program_id):
    concert_program = get_object_or_404(ConcertProgram, concert_program_id=concert_program_id)
    if request.method == "POST":
        concert_program.delete()
        return redirect('concert_programs')
    return redirect('concert_programs')

def edit_member_role(request, member_roles_id):
    member_role = get_object_or_404(MemberRoles, member_roles_id=member_roles_id)
    if request.method == "POST":
        form = MemberRolesForm(request.POST, instance=member_role)
        if form.is_valid():
            form.save()
            return redirect('member_roles')
    else:
        form = MemberRolesForm(instance=member_role)
    return render(request, 'edit_member_role.html', {'form': form})

def create_member_role(request):
    if request.method == "POST":
        form = MemberRolesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_roles')
    else:
        form = MemberRolesForm()
    return render(request, 'create_member_role.html', {'form': form})

def delete_member_role(request, member_roles_id):
    member_role = get_object_or_404(MemberRoles, member_roles_id=member_roles_id)
    if request.method == "POST":
        member_role.delete()
        return redirect('member_roles')
    return redirect('member_roles')

def edit_member_to_music_band(request, member_to_music_band_id):
    member_to_music_band = get_object_or_404(MemberToMusicBand, member_to_music_band_id=member_to_music_band_id)
    if request.method == "POST":
        form = MemberToMusicBandForm(request.POST, instance=member_to_music_band)
        if form.is_valid():
            form.save()
            return redirect('member_to_music_bands')
    else:
        form = MemberToMusicBandForm(instance=member_to_music_band)
    return render(request, 'edit_member_to_music_band.html', {'form': form})

def create_member_to_music_band(request):
    if request.method == "POST":
        form = MemberToMusicBandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_to_music_bands')
    else:
        form = MemberToMusicBandForm()
    return render(request, 'create_member_to_music_band.html', {'form': form})

def delete_member_to_music_band(request, member_to_music_band_id):
    member_to_music_band = get_object_or_404(MemberToMusicBand, member_to_music_band_id=member_to_music_band_id)
    if request.method == "POST":
        member_to_music_band.delete()
        return redirect('member_to_music_bands')
    return redirect('member_to_music_bands')

def edit_music_band_contract(request, music_band_contract_id):
    music_band_contract = get_object_or_404(MusicBandContract, music_band_contract_id=music_band_contract_id)
    if request.method == "POST":
        form = MusicBandContractForm(request.POST, instance=music_band_contract)
        if form.is_valid():
            form.save()
            return redirect('music_band_contracts')
    else:
        form = MusicBandContractForm(instance=music_band_contract)
    return render(request, 'edit_music_band_contract.html', {'form': form})

def create_music_band_contract(request):
    if request.method == "POST":
        form = MusicBandContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music_band_contracts')
    else:
        form = MusicBandContractForm()
    return render(request, 'create_music_band_contract.html', {'form': form})

def delete_music_band_contract(request, music_band_contract_id):
    music_band_contract = get_object_or_404(MusicBandContract, music_band_contract_id=music_band_contract_id)
    if request.method == "POST":
        music_band_contract.delete()
        return redirect('music_band_contracts')
    return redirect('music_band_contracts')

def edit_music_band(request, music_band_id):
    music_band = get_object_or_404(MusicBand, music_band_id=music_band_id)
    if request.method == "POST":
        form = MusicBandForm(request.POST, instance=music_band)
        if form.is_valid():
            form.save()
            return redirect('music_bands')
    else:
        form = MusicBandForm(instance=music_band)
    return render(request, 'edit_music_band.html', {'form': form})

def create_music_band(request):
    if request.method == "POST":
        form = MusicBandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music_bands')
    else:
        form = MusicBandForm()
    return render(request, 'create_music_band.html', {'form': form})

def delete_music_band(request, music_band_id):
    music_band = get_object_or_404(MusicBand, music_band_id=music_band_id)
    if request.method == "POST":
        music_band.delete()
        return redirect('music_bands')
    return redirect('music_bands')

