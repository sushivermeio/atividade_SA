# Generated by Django 4.1.3 on 2022-12-02 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrologin',
            name='horario_saida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]