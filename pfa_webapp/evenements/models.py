import sys

from django.db import models
from simple_history.models import HistoricalRecords

from clubs.models import Clubs

sys.path.append("..")


# Create your models here.
class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    name_event = models.CharField(max_length=50, unique=True, verbose_name="Nom événement")
    club = models.ForeignKey('clubs.Clubs', models.DO_NOTHING, db_column='club', blank=True, null=True,
                             related_name="evenementsClub", verbose_name="Club organisateur")
    date_event = models.DateField(blank=True, null=True, verbose_name="Date événement")
    duration = models.IntegerField(blank=True, null=True, verbose_name="Durée événement")
    budget = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True,
                                 verbose_name="Budget événement (sponsors + administration)")
    available_places = models.IntegerField(blank=True, null=True, verbose_name="Places disponibles")
    ticket_price = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True,
                                       verbose_name="Prix billet")

    history = HistoricalRecords()

    def get_tickets_event(self, Tickets):
        return Tickets.objects.filter(id_event=self.id_event)

    def calculate(self, queryset):
        return float((queryset) * self.ticket_price)

    def __str__(self):
        return 'Evénement: ' + self.name_event

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))

                if field.verbose_name != 'Club organisateur'

                else
                (field.verbose_name,
                 Clubs.objects.get(pk=field.value_from_object(self)).name_club)

                for field in self.__class__._meta.fields[1:]
                ]

    class Meta:
        managed = False
        db_table = 'events'
        verbose_name = 'Evénement'
        verbose_name_plural = 'Evénements'
