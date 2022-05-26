from django.db import models

# Create your models here.
class Purchases(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    article = models.CharField(max_length=50, blank=True, null=True)
    unitary_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    invoice_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Achat: ' + self.article

    class Meta:
        managed = False
        db_table = 'purchases'
        verbose_name = 'Achat'
        verbose_name_plural = 'Achats'