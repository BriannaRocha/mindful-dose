# Generated by Django 4.2.10 on 2024-03-07 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_dose'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dose',
            options={'ordering': ['-date']},
        ),
    ]
