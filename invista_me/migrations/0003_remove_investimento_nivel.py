# Generated by Django 5.1.6 on 2025-02-07 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0002_investimento_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='nivel',
        ),
    ]
