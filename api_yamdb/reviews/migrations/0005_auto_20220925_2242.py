# Generated by Django 2.2.16 on 2022-09-25 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220924_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['id'], 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]