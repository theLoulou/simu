# Generated by Django 2.0.4 on 2018-05-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0004_auto_20180512_0331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ag',
            name='id',
        ),
        migrations.AlterField(
            model_name='ag',
            name='policy_ID',
            field=models.DecimalField(decimal_places=1, max_digits=15, primary_key=True, serialize=False),
        ),
    ]
