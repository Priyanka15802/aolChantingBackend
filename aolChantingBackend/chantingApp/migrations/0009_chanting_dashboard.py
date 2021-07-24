# Generated by Django 3.2.5 on 2021-07-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chantingApp', '0008_chanting_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='chanting_dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chant_name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]