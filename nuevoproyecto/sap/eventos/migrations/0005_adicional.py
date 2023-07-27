# Generated by Django 4.2.2 on 2023-06-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_cliente_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decoracion', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, null=True)),
                ('musica', models.CharField(max_length=2, null=True)),
            ],
        ),
    ]
