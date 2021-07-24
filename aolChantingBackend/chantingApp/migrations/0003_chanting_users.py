# Generated by Django 3.2.5 on 2021-07-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chantingApp', '0002_delete_chanting_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='chanting_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField(blank=True, max_length=10, null=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
