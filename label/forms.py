from django import forms
from .models import (
    Members, MusicBand, ConcertHall, MemberRoles, ConcertHallContract,
    ConcertHallManager, ConcertProgram, MemberToMusicBand, MusicBandContract
)

class MemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'

class ConcertHallContractForm(forms.ModelForm):
    class Meta:
        model = ConcertHallContract
        fields = '__all__'

class ConcertHallManagerForm(forms.ModelForm):
    class Meta:
        model = ConcertHallManager
        fields = '__all__'

class ConcertHallForm(forms.ModelForm):
    class Meta:
        model = ConcertHall
        fields = '__all__'

class ConcertProgramForm(forms.ModelForm):
    class Meta:
        model = ConcertProgram
        fields = '__all__'

class MemberRolesForm(forms.ModelForm):
    class Meta:
        model = MemberRoles
        fields = '__all__'

class MemberToMusicBandForm(forms.ModelForm):
    class Meta:
        model = MemberToMusicBand
        fields = '__all__'

class MusicBandContractForm(forms.ModelForm):
    class Meta:
        model = MusicBandContract
        fields = '__all__'

class MusicBandForm(forms.ModelForm):
    class Meta:
        model = MusicBand
        fields = '__all__'
