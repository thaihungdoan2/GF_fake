# Generated by Django 2.2 on 2020-11-19 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakevaccine', '0002_auto_20201119_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiemphong',
            name='create_by',
            field=models.CharField(blank=True, default='doan', max_length=50),
        ),
    ]
