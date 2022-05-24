from django.db import models
from django.apps import apps
import sys
sys.path.append("..")
from etudiants.models import Students
from evenements.models import Events


# Create your models here.


class Tickets(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    id_event = models.ForeignKey(Events, models.DO_NOTHING, db_column='id_event', blank=True, null=True)
    id_student = models.ForeignKey(Students, models.DO_NOTHING, db_column='id_student', blank=True, null=True)
    presence = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return 'Ticket: ' + getattr(getattr(self, 'id_student'), 'name_student') + ' ' + getattr(getattr(self, 'id_event'), 'name_event')

    class Meta:
        managed = False
        db_table = 'tickets'
        verbose_name_plural = 'Tickets'