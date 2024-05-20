from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from .models import (
    Members, MusicBand, ConcertHall, MemberRoles, ConcertHallContract,
    ConcertHallManager, ConcertProgram, MemberToMusicBand, MusicBandContract
)
from .forms import (
    MemberForm, MusicBandForm, ConcertHallForm, MemberRolesForm, ConcertHallContractForm,
    ConcertHallManagerForm, ConcertProgramForm, MemberToMusicBandForm, MusicBandContractForm
)
# Create your views here.

@login_required
def index(request):
    user_permissions = request.user.get_all_permissions()
    context = {
        'user_permissions': user_permissions,
        'can_view_members': request.user.has_perm('label.view_members'),
        'can_view_music_bands': request.user.has_perm('label.view_musicband'),
        'can_view_concert_halls': request.user.has_perm('label.view_concerthall'),
        'can_view_member_roles': request.user.has_perm('label.view_memberroles'),
        'can_view_concert_hall_contracts': request.user.has_perm('label.view_concerthallcontract'),
        'can_view_concert_hall_managers': request.user.has_perm('label.view_concerthallmanager'),
        'can_view_concert_programs': request.user.has_perm('label.view_concertprogram'),
        'can_view_member_to_music_bands': request.user.has_perm('label.view_membertomusicband'),
        'can_view_music_band_contracts': request.user.has_perm('label.view_musicbandcontract'),
    }
    return render(
        request,
        'index.html', context
    )
@login_required
@permission_required('label.view_members', raise_exception=True)
def members(request):
    data = Members.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_members'),
        'can_change': request.user.has_perm('label.change_members'),
        'can_delete': request.user.has_perm('label.delete_members'),
    }
    return render(request, 'members.html', context)

@login_required
@permission_required('label.view_musicband', raise_exception=True)
def music_bands(request):
    data = MusicBand.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_musicband'),
        'can_change': request.user.has_perm('label.change_musicband'),
        'can_delete': request.user.has_perm('label.delete_musicband'),
    }
    return render(request, 'music_bands.html', context)

@login_required
@permission_required('label.view_concerthall', raise_exception=True)
def concert_halls(request):
    data = ConcertHall.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_concerthall'),
        'can_change': request.user.has_perm('label.change_concerthall'),
        'can_delete': request.user.has_perm('label.delete_concerthall'),
    }
    return render(request, 'concert_halls.html', context)

@login_required
@permission_required('label.view_memberroles', raise_exception=True)
def member_roles(request):
    data = MemberRoles.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_memberroles'),
        'can_change': request.user.has_perm('label.change_memberroles'),
        'can_delete': request.user.has_perm('label.delete_memberroles'),
    }
    return render(request, 'member_roles.html', context)

@login_required
@permission_required('label.view_concerthallcontract', raise_exception=True)
def concert_hall_contracts(request):
    data = ConcertHallContract.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_concerthallcontract'),
        'can_change': request.user.has_perm('label.change_concerthallcontract'),
        'can_delete': request.user.has_perm('label.delete_concerthallcontract'),
    }
    return render(request, 'concert_hall_contracts.html', context)

@login_required
@permission_required('label.view_concerthallmanager', raise_exception=True)
def concert_hall_managers(request):
    data = ConcertHallManager.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_concerthallmanager'),
        'can_change': request.user.has_perm('label.change_concerthallmanager'),
        'can_delete': request.user.has_perm('label.delete_concerthallmanager'),
    }
    return render(request, 'concert_hall_managers.html', context)

@login_required
@permission_required('label.view_concertprogram', raise_exception=True)
def concert_programs(request):
    data = ConcertProgram.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_concertprogram'),
        'can_change': request.user.has_perm('label.change_concertprogram'),
        'can_delete': request.user.has_perm('label.delete_concertprogram'),
    }
    return render(request, 'concert_programs.html', context)

@login_required
@permission_required('label.view_membertomusicband', raise_exception=True)
def member_to_music_bands(request):
    data = MemberToMusicBand.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_membertomusicband'),
        'can_change': request.user.has_perm('label.change_membertomusicband'),
        'can_delete': request.user.has_perm('label.delete_membertomusicband'),
    }
    return render(request, 'member_to_music_bands.html', context)

@login_required
@permission_required('label.view_musicbandcontract', raise_exception=True)
def music_band_contracts(request):
    data = MusicBandContract.objects.all()
    context = {
        'data': data,
        'can_add': request.user.has_perm('label.add_musicbandcontract'),
        'can_change': request.user.has_perm('label.change_musicbandcontract'),
        'can_delete': request.user.has_perm('label.delete_musicbandcontract'),
    }
    return render(request, 'music_band_contracts.html', context)

@login_required
@permission_required('label.change_members', raise_exception=True)
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


@login_required
@permission_required('label.add_members', raise_exception=True)
def create_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm()
    return render(request, 'create_member.html', {'form': form})

@login_required
@permission_required('label.delete_members', raise_exception=True)
def delete_member(request, members_id):
    member = get_object_or_404(Members, members_id=members_id)
    if request.method == "POST":
        member.delete()
        return redirect('members')
    return redirect('members')

@login_required
@permission_required('label.change_concerthallcontract', raise_exception=True)
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

@login_required
@permission_required('label.add_concerthallcontract', raise_exception=True)
def create_concert_hall_contract(request):
    if request.method == "POST":
        form = ConcertHallContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_hall_contracts')
    else:
        form = ConcertHallContractForm()
    return render(request, 'create_concert_hall_contract.html', {'form': form})

@login_required
@permission_required('label.delete_concerthallcontract', raise_exception=True)
def delete_concert_hall_contract(request, concert_hall_contract_id):
    concert_hall_contracts = get_object_or_404(ConcertHallContract, concert_hall_contract_id=concert_hall_contract_id)
    if request.method == "POST":
        concert_hall_contracts.delete()
        return redirect('concert_hall_contracts')
    return redirect('concert_hall_contracts')

@login_required
@permission_required('label.change_concerthallmanager', raise_exception=True)
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

@login_required
@permission_required('label.add_concerthallmanager', raise_exception=True)
def create_concert_hall_manager(request):
    if request.method == "POST":
        form = ConcertHallManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_hall_managers')
    else:
        form = ConcertHallManagerForm()
    return render(request, 'create_concert_hall_manager.html', {'form': form})

@login_required
@permission_required('label.delete_concerthallmanager', raise_exception=True)
def delete_concert_hall_manager(request, concert_hall_manager_id):
    concert_hall_managers = get_object_or_404(ConcertHallManager, concert_hall_manager_id=concert_hall_manager_id)
    if request.method == "POST":
        concert_hall_managers.delete()
        return redirect('concert_hall_managers')
    return redirect('concert_hall_managers')

@login_required
@permission_required('label.change_concerthall', raise_exception=True)
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

@login_required
@permission_required('label.add_concerthall', raise_exception=True)
def create_concert_hall(request):
    if request.method == "POST":
        form = ConcertHallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_halls')
    else:
        form = ConcertHallForm()
    return render(request, 'create_concert_hall.html', {'form': form})

@login_required
@permission_required('label.delete_concerthall', raise_exception=True)
def delete_concert_hall(request, concert_hall_id):
    concert_hall = get_object_or_404(ConcertHall, concert_hall_id=concert_hall_id)
    if request.method == "POST":
        concert_hall.delete()
        return redirect('concert_halls')
    return redirect('concert_halls')

@login_required
@permission_required('label.change_concertprogram', raise_exception=True)
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

@login_required
@permission_required('label.add_concertprogram', raise_exception=True)
def create_concert_program(request):
    if request.method == "POST":
        form = ConcertProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concert_programs')
    else:
        form = ConcertProgramForm()
    return render(request, 'create_concert_program.html', {'form': form})

@login_required
@permission_required('label.delete_concertprogram', raise_exception=True)
def delete_concert_program(request, concert_program_id):
    concert_program = get_object_or_404(ConcertProgram, concert_program_id=concert_program_id)
    if request.method == "POST":
        concert_program.delete()
        return redirect('concert_programs')
    return redirect('concert_programs')

@login_required
@permission_required('label.change_memberroles', raise_exception=True)
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

@login_required
@permission_required('label.add_memberroles', raise_exception=True)
def create_member_role(request):
    if request.method == "POST":
        form = MemberRolesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_roles')
    else:
        form = MemberRolesForm()
    return render(request, 'create_member_role.html', {'form': form})

@login_required
@permission_required('label.delete_memberroles', raise_exception=True)
def delete_member_role(request, member_roles_id):
    member_role = get_object_or_404(MemberRoles, member_roles_id=member_roles_id)
    if request.method == "POST":
        member_role.delete()
        return redirect('member_roles')
    return redirect('member_roles')

@login_required
@permission_required('label.change_membertomusicband', raise_exception=True)
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

@login_required
@permission_required('label.add_membertomusicband', raise_exception=True)
def create_member_to_music_band(request):
    if request.method == "POST":
        form = MemberToMusicBandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_to_music_bands')
    else:
        form = MemberToMusicBandForm()
    return render(request, 'create_member_to_music_band.html', {'form': form})

@login_required
@permission_required('label.delete_membertomusicband', raise_exception=True)
def delete_member_to_music_band(request, member_to_music_band_id):
    member_to_music_band = get_object_or_404(MemberToMusicBand, member_to_music_band_id=member_to_music_band_id)
    if request.method == "POST":
        member_to_music_band.delete()
        return redirect('member_to_music_bands')
    return redirect('member_to_music_bands')

@login_required
@permission_required('label.change_musicbandcontract', raise_exception=True)
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

@login_required
@permission_required('label.add_musicbandcontract', raise_exception=True)
def create_music_band_contract(request):
    if request.method == "POST":
        form = MusicBandContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music_band_contracts')
    else:
        form = MusicBandContractForm()
    return render(request, 'create_music_band_contract.html', {'form': form})

@login_required
@permission_required('label.delete_musicbandcontract', raise_exception=True)
def delete_music_band_contract(request, music_band_contract_id):
    music_band_contract = get_object_or_404(MusicBandContract, music_band_contract_id=music_band_contract_id)
    if request.method == "POST":
        music_band_contract.delete()
        return redirect('music_band_contracts')
    return redirect('music_band_contracts')

@login_required
@permission_required('label.change_musicband', raise_exception=True)
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

@login_required
@permission_required('label.add_musicband', raise_exception=True)
def create_music_band(request):
    if request.method == "POST":
        form = MusicBandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music_bands')
    else:
        form = MusicBandForm()
    return render(request, 'create_music_band.html', {'form': form})

@login_required
@permission_required('label.delete_musicband', raise_exception=True)
def delete_music_band(request, music_band_id):
    music_band = get_object_or_404(MusicBand, music_band_id=music_band_id)
    if request.method == "POST":
        music_band.delete()
        return redirect('music_bands')
    return redirect('music_bands')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
