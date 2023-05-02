# Generated by Django 4.2 on 2023-05-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('produto', models.CharField(max_length=50)),
                ('solicitante', models.CharField(max_length=50)),
                ('seguradora', models.CharField(max_length=50)),
                ('carro_rebocado', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=10)),
                ('sinistro', models.CharField(max_length=10)),
                ('tot_km', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('de', models.CharField(max_length=100)),
                ('para', models.CharField(max_length=100)),
            ],
        ),
    ]