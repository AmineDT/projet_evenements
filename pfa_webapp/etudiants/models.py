from django.db import models

# Create your models here.
class Students(models.Model):
    id_student = models.AutoField(primary_key=True)
    name_student = models.CharField(max_length=25)
    surname_student = models.CharField(max_length=25)
    study_field = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return 'Etudiant: ' + self.name_student + ' ' + self.surname_student

    class Meta:
        managed = False
        db_table = 'students'
        verbose_name_plural = 'Students'
