# Generated by Django 5.1 on 2024-09-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(blank=True, help_text='manufacturing date', null=True, verbose_name='Дата производства'),
        ),
    ]
