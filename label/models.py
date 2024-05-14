from django.db import models

# Create your models here.

class Members(models.Model):
    members_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12)

    class Meta:
        db_table = 'members'

class MusicBand(models.Model):
    music_band_id = models.AutoField(primary_key=True)
    music_band_name = models.CharField(max_length=50)
    music_genre = models.CharField(max_length=50)
    foundation_date = models.DateField()
    members_quantity = models.IntegerField()

    class Meta:
        db_table = 'music_band'

class ConcertHall(models.Model):
    concert_hall_id = models.AutoField(primary_key=True)
    concert_hall_name = models.CharField(max_length=50)
    address = models.CharField(max_length=75)
    quantity_of_people = models.IntegerField()
    avg_ticket_price = models.IntegerField()
    bar_availability = models.IntegerField()
    ticket_revenue_percent = models.IntegerField()
    hall_square_area = models.IntegerField()

    class Meta:
        db_table = 'concert_hall'

class MemberRoles(models.Model):
    member_roles_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'member_roles'

class ConcertHallContract(models.Model):
    concert_hall_contract_id = models.AutoField(primary_key=True)
    concert_hall = models.ForeignKey('ConcertHall', on_delete=models.PROTECT, db_column='concert_hall')
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()

    class Meta:
        db_table = 'concert_hall_contract'

class ConcertHallManager(models.Model):
    concert_hall_manager_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12)
    concert_hall = models.ForeignKey('ConcertHall', on_delete=models.PROTECT, db_column='concert_hall')

    class Meta:
        db_table = 'concert_hall_manager'

class ConcertProgram(models.Model):
    concert_program_id = models.AutoField(primary_key=True)
    concert_date = models.DateField()
    concert_start_time = models.TimeField()
    concert_end_time = models.TimeField()
    music_band = models.ForeignKey('MusicBand', on_delete=models.PROTECT, db_column='music_band', blank=True, null=True)
    concert_hall = models.ForeignKey('ConcertHall', on_delete=models.PROTECT, db_column='concert_hall', blank=True, null=True)

    class Meta:
        db_table = 'concert_program'

class MemberToMusicBand(models.Model):
    member_to_music_band_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('Members', on_delete=models.PROTECT, db_column='member')
    music_band = models.ForeignKey('MusicBand', on_delete=models.PROTECT, db_column='music_band')
    member_role = models.ForeignKey('MemberRoles', on_delete=models.PROTECT, db_column='member_role')
    member_join_date = models.DateField()

    class Meta:
        db_table = 'member_to_music_band'

class MusicBandContract(models.Model):
    music_band_contract_id = models.AutoField(primary_key=True)
    music_band = models.ForeignKey('MusicBand', on_delete=models.PROTECT, db_column='music_band')
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()

    class Meta:
        db_table = 'music_band_contract'

