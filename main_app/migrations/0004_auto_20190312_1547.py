# Generated by Django 2.1.5 on 2019-03-12 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190312_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['track_num']},
        ),
    ]