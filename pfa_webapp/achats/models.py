import sys

from django.db import models
from simple_history.models import HistoricalRecords
from utilisateurs.models import UserProfile

sys.path.append("..")
from clubs.models import Clubs
from evenements.models import Events


# Create your models here.
class Purchases(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    article = models.CharField(max_length=50, blank=True, null=True, verbose_name="article")
    unitary_cost = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True,
                                       verbose_name="Coût unitaire")
    quantity = models.IntegerField(blank=True, null=True, verbose_name="Quantité")
    purchase_date = models.DateField(blank=True, null=True, verbose_name="Date achat")
    invoice_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Numéro de facture")
    id_club = models.ForeignKey(Clubs, models.DO_NOTHING, db_column='id_club', verbose_name="Club")
    id_event = models.ForeignKey(Events, models.DO_NOTHING, db_column='id_event', blank=True, null=True,
                                 verbose_name="Evénement")
    owner_obj = models.ForeignKey(UserProfile, models.DO_NOTHING, db_column='owner_obj', blank=True,
                                  null=True)
    history = HistoricalRecords()

    def __str__(self):
        return 'Achat: ' + self.article

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))

                if field.verbose_name != 'purchase'

                else
                (field.verbose_name,
                 Purchases.objects.get(pk=field.value_from_object(self)).name)

                for field in self.__class__._meta.fields[1:]
                ]

    class Meta:
        managed = False
        db_table = 'purchases'
        verbose_name = 'Achat'
        verbose_name_plural = 'Achats'
