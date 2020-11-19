from django.contrib import admin

# Register your models here.
from .models import HeoCon, HeoMe, HeoAll

admin.site.register(HeoCon)
admin.site.register(HeoMe)
admin.site.register(HeoAll)
