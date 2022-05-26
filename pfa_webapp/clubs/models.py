from django.db import models
import django_tables2 as tables


# Create your models here.
class Club(models.Model):
    id_club = models.AutoField(primary_key=True)
    name_club = models.CharField(max_length=50, unique=True, verbose_name="Nom club")
    description = models.TextField(null=True, blank=True, verbose_name="Description")

    def __str__(self):
        return 'Club: ' + self.name_club

    class Meta:
        managed = False
        db_table = 'clubs'
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

