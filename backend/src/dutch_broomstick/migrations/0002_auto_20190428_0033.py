# Generated by Django 2.2 on 2019-04-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dutch_broomstick', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='default_account',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='default_nickname',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]