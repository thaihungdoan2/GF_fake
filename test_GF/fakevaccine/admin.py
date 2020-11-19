from django.contrib import admin

# Register your models here.
from .models import Vaccine, Tiemphong

admin.site.register(Vaccine)
admin.site.register(Tiemphong)
