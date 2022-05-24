# Generated by Django 4.0.4 on 2022-05-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id_club', models.AutoField(primary_key=True, serialize=False)),
                ('name_club', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Clubs',
                'db_table': 'clubs',
                'managed': False,
            },
        ),
    ]