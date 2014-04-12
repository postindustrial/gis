from django.contrib import admin
from cargo.models import Cargo

class CargoAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight')
    list_filter = ('name',)

admin.site.register(Cargo, CargoAdmin)