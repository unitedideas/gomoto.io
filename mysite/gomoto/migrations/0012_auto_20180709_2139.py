# Generated by Django 2.0.6 on 2018-07-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomoto', '0011_auto_20180709_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='weight',
            new_name='dry_weight',
        ),
        migrations.AddField(
            model_name='bike',
            name='wet_weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]