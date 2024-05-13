from django.db import models

# Create your models here.

class Members(models.Model):
    members_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=11)

    class Meta:
        db_table = 'members'