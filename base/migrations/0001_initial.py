# Generated by Django 4.2.7 on 2023-12-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('matric_number', models.CharField(max_length=8)),
                ('college', models.CharField(choices=[('Colphys', 'Colphys'), ('Colbios', 'Colbios'), ('Colerm', 'Colerm'), ('Coleng', 'Coleng'), ('Colfhec', 'Colfhec'), ('Colanim', 'Colanim'), ('Colplant', 'Colplant'), ('Colamrud', 'Colamrud')], max_length=50)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
    ]
