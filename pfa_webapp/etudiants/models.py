from django.db import models

# Create your models here.
class Students(models.Model):
    id_student = models.AutoField(primary_key=True)
    name_student = models.CharField(max_length=25, verbose_name="Nom étudiant")
    surname_student = models.CharField(max_length=25, verbose_name="Prénom")
    study_field = models.CharField(max_length=50, blank=True, null=True, verbose_name="Specialité")
    email = models.CharField(max_length=35, blank=True, null=True, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Téléphone")

    def __str__(self):
        return 'Etudiant: ' + self.name_student + ' ' + self.surname_student

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))

                if field.verbose_name != 'event'

                else
                (field.verbose_name,
                 Students.objects.get(pk=field.value_from_object(self)).name)

                for field in self.__class__._meta.fields[1:]
                ]


    class Meta:
        managed = False
        db_table = 'students'
        verbose_name = 'Etudiant'
        verbose_name_plural = 'Etudiants'
