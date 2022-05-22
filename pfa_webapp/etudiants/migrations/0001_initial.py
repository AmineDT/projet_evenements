# Generated by Django 4.0.4 on 2022-05-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id_student', models.AutoField(primary_key=True, serialize=False)),
                ('name_student', models.CharField(max_length=25)),
                ('surname_student', models.CharField(max_length=25)),
                ('study_field', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=35, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
    ]
