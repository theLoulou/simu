# Generated by Django 2.0.4 on 2018-05-10 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ag_breedC', models.BooleanField()),
                ('policy_ID', models.BigIntegerField()),
                ('age', models.PositiveSmallIntegerField()),
                ('social_grade', models.PositiveSmallIntegerField()),
                ('Payment', models.PositiveSmallIntegerField()),
                ('attribute_brand', models.DecimalField(decimal_places=1, max_digits=3)),
                ('attribute_price', models.DecimalField(decimal_places=1, max_digits=3)),
                ('attribute_promotion', models.DecimalField(decimal_places=1, max_digits=3)),
                ('auto_renew', models.BooleanField()),
                ('inertia_switch', models.PositiveSmallIntegerField()),
                ('change', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Agent',
                'ordering': ['Ag_breedC'],
            },
        ),
    ]
