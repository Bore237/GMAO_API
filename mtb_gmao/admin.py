from django.contrib import admin

# Register your models here.

from .models import Person, Societe, Stock, Operation, Machine

class PersonAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'date_create')
    #list_filter = ('band',)

admin.site.register(Societe)  # Use the default options
admin.site.register(Stock)  # Use the default options
admin.site.register(Operation)  # Use the default options
admin.site.register(Machine)  # Use the default options
admin.site.register(Person, PersonAdmin)  # Use the customized options
      