from django.contrib import admin

from .models import Wojewodztwo, Powiat_Miasto, Gmina_Miasto, Obwod

admin.site.register(Wojewodztwo)
admin.site.register(Powiat_Miasto)
admin.site.register(Gmina_Miasto)
admin.site.register(Obwod)