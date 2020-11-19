from django.db import models

# Create your models here.
from fakeheo.models import HeoAll

class Vaccine(models.Model):
    id_vaccine = models.CharField(primary_key=True,max_length=50,unique=True)
    name_vaccine = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    create_at = models.DateField(auto_now=False, auto_now_add=False)
    create_by = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id_vaccine)

class Tiemphong(models.Model):
    Vaccine = models.ForeignKey("Vaccine", on_delete=models.CASCADE, blank=True, null=True)
    RFID = models.ForeignKey("fakeheo.HeoAll", on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateField( auto_now_add=True)
    create_by = models.CharField(max_length=50, default="doan", blank=True)
    def __str__(self):
        return str(self.RFID)
