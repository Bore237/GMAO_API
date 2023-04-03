from django.contrib import admin

# Register your models here.

from .models import Person, Societe, Stock, Operation, Machine


class SioceteAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Personnal Information", {"fields": ["name", "email", "type_societe", "imatriculation"]}),
        ("Localisation",{"fields": ["siege_social", "phone", "gps_pos"]}),
        ("Sercice Compagny", {"fields": ["activite", "contrat"]}),
    ]
    list_display = ["name", "email", "type_societe", "imatriculation",
                     "siege_social", "phone", "gps_pos", "activite", "contrat"]
    list_filter = ["name", "type_societe"]

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Personnal Information", {"fields": ["name", "prenom", "date_birth", "email"]}),
        ( "Localisation",{"fields": ["residence","phone", "gps_pos"]}),
        ("Company information", {"fields": ["nom_societe", "salaire", "type_contract"]}),
    ]
    list_display = ["name", "prenom","date_birth", "email", "phone",
                     "nom_societe", "residence", "salaire", "type_contract" ]
    list_filter = ["name", "nom_societe"]

admin.site.register(Societe, SioceteAdmin)  
admin.site.register(Person, PersonAdmin)  
admin.site.register(Stock)  # Use the default options
admin.site.register(Operation)  # Use the default options
admin.site.register(Machine)  # Use the default options

      