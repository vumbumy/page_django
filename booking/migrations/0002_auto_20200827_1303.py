# Generated by Django 3.1 on 2020-08-27 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-date_from']},
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='data_from',
            new_name='date_from',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='data_to',
            new_name='date_to',
        ),
    ]
