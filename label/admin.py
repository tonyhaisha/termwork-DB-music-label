from django.contrib import admin
from .models import Members, MemberRoles, MemberToMusicBand, MusicBand, MusicBandContract, ConcertHallContract, ConcertHall, ConcertHallManager, ConcertProgram

# Register your models here.
admin.site.register(Members)
admin.site.register(MemberRoles)
admin.site.register(MemberToMusicBand)
admin.site.register(MusicBand)
admin.site.register(MusicBandContract)
admin.site.register(ConcertHallContract)
admin.site.register(ConcertHall)
admin.site.register(ConcertHallManager)
admin.site.register(ConcertProgram)
