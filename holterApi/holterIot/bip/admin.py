from django.contrib import admin

# Register your models here.

from .models import Profiles, patientData, Token , MyModel
# Register your models here.

admin.site.register(Profiles)
admin.site.register(patientData)
admin.site.register(Token)

admin.site.register(DataPlot)