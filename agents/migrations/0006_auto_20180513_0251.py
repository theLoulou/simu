# Generated by Django 2.0.4 on 2018-05-13 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0005_auto_20180512_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='ag',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ag',
            name='policy_ID',
            field=models.DecimalField(decimal_places=1, max_digits=15),
        ),
    ]
