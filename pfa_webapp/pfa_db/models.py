from django.db import models
from django.urls import reverse

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    name_event = models.CharField(max_length=-1)
    id_label = models.ForeignKey('Label', models.DO_NOTHING, db_column='id_label', blank=True, null=True)
    date_event = models.DateField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    budget = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    available_places = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Label(models.Model):
    id_label = models.AutoField(primary_key=True)
    name_label = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label'


class Purchases(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    article = models.CharField(max_length=-1, blank=True, null=True)
    unitary_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    invoice_number = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchases'


class Students(models.Model):
    id_student = models.AutoField(primary_key=True)
    name_student = models.CharField(max_length=-1)
    surname_student = models.CharField(max_length=-1)
    study_field = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Tickets(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    id_event = models.ForeignKey(Events, models.DO_NOTHING, db_column='id_event', blank=True, null=True)
    id_student = models.ForeignKey(Students, models.DO_NOTHING, db_column='id_student', blank=True, null=True)
    ticket_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    presence = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'
