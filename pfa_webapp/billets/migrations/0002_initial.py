# Generated by Django 4.0.4 on 2022-05-31 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('evenements', '0001_initial'),
        ('etudiants', '0001_initial'),
        ('billets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltickets',
            name='id_event',
            field=models.ForeignKey(blank=True, db_column='id_event', db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to='evenements.events', verbose_name='Evénement'),
        ),
        migrations.AddField(
            model_name='historicaltickets',
            name='id_student',
            field=models.ForeignKey(blank=True, db_column='id_student', db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to='etudiants.students', verbose_name='Etudiant'),
        ),
    ]
