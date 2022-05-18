from django.db import models


# Create your models here.

class Students(models.Model):
    id_student = models.AutoField(primary_key=True)
    name_student = models.CharField(max_length=-1)
    surname_student = models.CharField(max_length=-1)
    study_field = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)


class Label(models.Model):
    id_label = models.AutoField(primary_key=True)
    name_label = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)


class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    name_event = models.CharField(max_length=-1)
    id_label = models.ForeignKey('Label', models.DO_NOTHING, db_column='id_label', blank=True, null=True)
    date_event = models.DateField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    budget = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    available_places = models.IntegerField(blank=True, null=True)


class Purchases(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    article = models.CharField(max_length=-1, blank=True, null=True)
    unitary_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    invoice_number = models.CharField(max_length=-1, blank=True, null=True)



class Tickets(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    id_event = models.ForeignKey(Events, models.DO_NOTHING, db_column='id_event', blank=True, null=True)
    id_student = models.ForeignKey(Students, models.DO_NOTHING, db_column='id_student', blank=True, null=True)
    ticket_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    presence = models.BooleanField(blank=True, null=True)


