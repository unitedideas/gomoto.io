# Generated by Django 2.0.6 on 2018-07-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobosevents', '0010_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='userevent',
            name='confirmation',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
