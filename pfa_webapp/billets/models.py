import sys

from django.db import models

sys.path.append("..")
from etudiants.models import Students
from evenements.models import Events
from simple_history.models import HistoricalRecords


# Create your models here.


class Tickets(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    id_event = models.ForeignKey(Events, models.DO_NOTHING, db_column='id_event', blank=True, null=True,
                                 related_name="ticketsEvenement", verbose_name="Evénement")
    id_student = models.ForeignKey(Students, models.DO_NOTHING, db_column='id_student', blank=True, null=True,
                                   verbose_name="Etudiant")

    history = HistoricalRecords()

    def __str__(self):
        return 'Ticket: ' + getattr(getattr(self, 'id_student'), 'name_student') + ' ' + getattr(
            getattr(self, 'id_event'), 'name_event')

    def get_fields(self):
        return [(field.verbose_name, Events.objects.get(pk=field.value_from_object(self)).name_event)

                if field.verbose_name != 'Etudiant'

                else
                (field.verbose_name,
                 str(Students.objects.get(pk=field.value_from_object(self)).name_student) + " " + str(
                     Students.objects.get(pk=field.value_from_object(self)).surname_student))

                for field in self.__class__._meta.fields[1:]
                ]


    class Meta:
        managed = False
        verbose_name = 'Billet'
        verbose_name_plural = 'Billets'
