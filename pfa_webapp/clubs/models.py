from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class Clubs(models.Model):
    id_club = models.AutoField(primary_key=True)
    name_club = models.CharField(max_length=50, unique=True, verbose_name="Nom club")
    description = models.TextField(null=True, blank=True, verbose_name="Description")

    history = HistoricalRecords()

    def __str__(self):
        return 'Club: ' + self.name_club

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))

                if field.verbose_name != 'clubs'

                else
                (field.verbose_name,
                 Clubs.objects.get(pk=field.value_from_object(self)).name)

                for field in self.__class__._meta.fields[1:]
                ]

    class Meta:
        managed = False
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'
