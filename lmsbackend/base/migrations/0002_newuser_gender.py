# Generated by Django 3.2.9 on 2021-11-30 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='gender',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]