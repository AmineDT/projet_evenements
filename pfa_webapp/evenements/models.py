from django.db import models
import sys
sys.path.append("..")
from clubs.models import Clubs

# Create your models here.
class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    name_event = models.CharField(max_length=50, unique=True, verbose_name="Nom événement")
    club = models.ForeignKey('clubs.Clubs', models.DO_NOTHING, db_column='club', blank=True, null=True, verbose_name="Club organisateur")
    date_event = models.DateField(blank=True, null=True,verbose_name="Date événement")
    duration = models.IntegerField(blank=True, null=True, verbose_name="Durée événement")
    budget = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True, verbose_name="Budget événement")
    available_places = models.IntegerField(blank=True, null=True, verbose_name="Places disponibles")
    ticket_price = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True, verbose_name="Prix billet")

    def __str__(self):
        return 'Evénement: ' + self.name_event

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))

                if field.verbose_name != 'event'

                else
                (field.verbose_name,
                 Events.objects.get(pk=field.value_from_object(self)).name)

                for field in self.__class__._meta.fields[1:]
                ]



    class Meta:
        managed = False
        db_table = 'events'
        verbose_name = 'Evénement'
        verbose_name_plural = 'Evénements'
