# Generated by Django 2.2 on 2020-11-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakevaccine', '0003_auto_20201119_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='id_vaccine',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]