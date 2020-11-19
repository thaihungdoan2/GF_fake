from django.db import models

# Create your models here.
HEO_CHOICES = (
    ("1", "Heocon"),
    ("2", "Heome"),
    ("3", "Heonai"),
)


class HeoMe(models.Model):
    # id = models.IntegerField(primary_key=True)
    name_heome = models.CharField(max_length=50, blank=True, null=True)
    rfid_heome = models.CharField(max_length=50, blank=True, null=True)
    chuong = models.IntegerField()

    def __str__(self):
        return str(self.id)


class HeoCon(models.Model):
    # id_heocon = models.IntegerField(primary_key=True)
    id_heome = models.ForeignKey(
        'HeoMe', on_delete=models.CASCADE, blank=True, null=True)
    rfid_heome = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    rfid_heocon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.rfid_heocon)


class HeoAll(models.Model):
    rfid = models.CharField(primary_key=True, max_length=50)
    type = models.CharField(
        max_length=2,
        choices=HEO_CHOICES,)

    def __str__(self):
        return str(self.rfid)
