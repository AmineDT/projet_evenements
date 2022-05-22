from django.db import models
import sys
sys.path.append("..")
from labels.models import Label

# Create your models here.
class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    name_event = models.CharField(max_length=50)
    id_label = models.ForeignKey('labels.Label', models.DO_NOTHING, db_column='id_label', blank=True, null=True)
    date_event = models.DateField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    budget = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    available_places = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'Evénement: ' + self.name_event

    class Meta:
        managed = False
        db_table = 'events'
        verbose_name_plural = 'Events'