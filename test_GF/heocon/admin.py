from django.contrib import admin

# Register your models here.
from .models import Herd, HeoCon, Finances

admin.site.register(Herd)
admin.site.register(HeoCon)
admin.site.register(Finances)
