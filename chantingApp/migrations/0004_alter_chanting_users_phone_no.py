# Generated by Django 3.2.5 on 2021-07-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chantingApp', '0003_chanting_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanting_users',
            name='phone_no',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
    ]
