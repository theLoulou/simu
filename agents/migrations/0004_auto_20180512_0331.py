# Generated by Django 2.0.4 on 2018-05-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_auto_20180511_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ag_evo',
            name='ID',
        ),
        migrations.AlterModelOptions(
            name='ag',
            options={},
        ),
        migrations.AddField(
            model_name='ag',
            name='results',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Ag_evo',
        ),
    ]
