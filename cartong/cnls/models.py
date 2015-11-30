# Register your models here.
from django.contrib import admin
#Activer l une ou l autre des 2 instruction ci dessous JPN 13/10/2015
#from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from models import Organisme, Utilisateur, Action, Typeintervention, Status,Cible,ActionCible,ActionTypeintervention,ActionLocalisation

#class ActionAdmin(admin.ModelAdmin):
#    fields = ['Typeinterventions', 'titre', 'date', 'duree', 'description', 'localisation', 'illustration',  'responsable', 'Avancement', 'Organisme']
#    list_display = ('get_Typeinterventions', 'titre', 'Organisme', 'date', 'duree', 'description', 'localisation', 'illustration', 'responsable', #'Avancement', 'creation', 'maj')
#    def get_Typeinterventions(self, obj):
#        return "\n".join([c.nom for c in obj.Typeinterventions.all()])
#    list_editable = ('titre', 'date', 'duree', 'description', 'localisation', 'illustration', 'responsable', 'Avancement')  #  Any field in #list_editable must also be in list_display. You can't edit a field that's not displayed!
#    list_filter = ('Typeinterventions', 'Organisme', 'localisation', 'Avancement')
#    search_fields = ['titre', 'description','get_Typeinterventions']
#    readonly_fields = ('creation', 'maj')
#    #list_display_links = ('region', 'Typeinterventions')  # The same field can't be listed in both list_editable and list_display_links -- a field #can't be both a form and a link.

class CibleAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

class TypeinterventionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

class ActionCibleAdmin(admin.TabularInline):
    model = ActionCible

class ActionTypeinterventionAdmin(admin.TabularInline):
    model = ActionTypeintervention  

class ActionLocalisationAdmin(admin.TabularInline):
    model = ActionLocalisation  
#    fields = ['region_status','fokontany','region',]
    list_display = ['region_status','fokontany','region',]
    

class ActionAdmin(admin.ModelAdmin):
    model = Action
    radio_fields = {"echelle_localisation": admin.VERTICAL}
    inlines = [ActionCibleAdmin,ActionTypeinterventionAdmin,ActionLocalisationAdmin,]



#admin.site.register(mdgRegion, admin.OSMGeoAdmin)
#admin.site.register(mdgRegion, LeafletGeoAdmin)
admin.site.register(Organisme)
admin.site.register(Utilisateur)
admin.site.register(ActionLocalisation)
#Activer l une ou l autre des 2 instructions ci dessous JPN 13/10/2015
#admin.site.register(Action)
admin.site.register(Action, ActionAdmin)
#admin.site.register(Action, LeafletGeoAdmin)
admin.site.register(Typeintervention,TypeinterventionAdmin)

admin.site.register(Status)
admin.site.register(Cible,CibleAdmin)
