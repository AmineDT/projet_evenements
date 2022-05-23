from django.db import models

# Create your models here.
class Label(models.Model):
    id_label = models.AutoField(primary_key=True)
    name_label = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Label: ' + self.name_label

    class Meta:
        managed = False
        db_table = 'label'
        verbose_name_plural = 'Labels'


