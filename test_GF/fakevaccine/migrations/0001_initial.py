# Generated by Django 2.2 on 2020-11-18 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fakeheo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id_vaccine', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name_vaccine', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('create_at', models.DateField()),
                ('create_by', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tiemphong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField()),
                ('create_by', models.CharField(max_length=50)),
                ('RFID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fakeheo.HeoAll')),
                ('Vaccine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fakevaccine.Vaccine')),
            ],
        ),
    ]
