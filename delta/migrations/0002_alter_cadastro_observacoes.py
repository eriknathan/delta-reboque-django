# Generated by Django 4.2 on 2023-05-03 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='observacoes',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]