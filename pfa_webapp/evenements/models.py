from django.db import models
import sys


sys.path.append("..")
from clubs.models import Club

# Create your models here.
class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    name_event = models.CharField(max_length=50, unique=True)
    club = models.ForeignKey('clubs.Club', models.DO_NOTHING, db_column='club', blank=True, null=True)
    date_event = models.DateField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    budget = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    available_places = models.IntegerField(blank=True, null=True)
    ticket_price = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return 'Evénement: ' + self.name_event

    class Meta:
        managed = False
        db_table = 'events'
        verbose_name = 'Evénement'
        verbose_name_plural = 'Evénements'
