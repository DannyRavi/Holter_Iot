from django.contrib import admin

# Register your models here.

from .models import Profiles, Token , DataPlot
# Register your models here.

admin.site.register(Profiles)
#admin.site.register(patientData)
admin.site.register(Token)

admin.site.register(DataPlot)