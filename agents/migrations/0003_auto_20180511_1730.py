# Generated by Django 2.0.4 on 2018-05-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_auto_20180511_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ag',
            name='policy_ID',
            field=models.DecimalField(decimal_places=1, max_digits=15),
        ),
    ]