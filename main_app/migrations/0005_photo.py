# Generated by Django 4.2.11 on 2024-03-08 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_drug_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.drug')),
            ],
        ),
    ]