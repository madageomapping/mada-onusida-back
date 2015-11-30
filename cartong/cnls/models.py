#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.gis.db import models as gismodels
from django.contrib.auth.models import User
from django.utils.timezone import now

"""
# Create your models here.
# Les "Primary Key" de chaque classe sont générées automatiquement 
"""
class Status(models.Model):
    ChoixStatus = (
    	(u'Partenaire sur une Action', u'Partenaire'),
        (u'Bailleur', u'Bailleur'),
        (u'''Organisme maître d'oeuvre''', u'Organisme'),
    )
    nom = models.CharField(max_length=40, choices=ChoixStatus, unique=True)
    
    class Meta:
        verbose_name_plural = "Status"
    
    def __unicode__(self):
        return u"Status: %s" % self.nommadageomapping

REGION_STATUS = (
    (0, '  '),
    (1, 'Oui'),
    (2, 'Non')              
)



DEVISE = (
    	(u'MGA', u'MGA'),
        (u'EUR', u'EUR'),
        (u'USD', u'USD'),
    )
    
ECHELLE_LOCALISATION = (
    	(u'nationale', u'Nationale'),
        (u'régionale', u'Régionale'),
        (u'locale', u'Locale'),
    )

AVANCEMENT = (
        (u'En attente', u'En attente'),
        (u'En cours', u'En cours'),
        (u'Terminé', u'Terminé'),
    )

# Cible
class Cible(models.Model):
    
    LISTE_CIBLES= (
        (u'population générale', u'Population générale'),
        (u'adultes', u'Adultes'),
        (u'personnes vivant avec le vih', u'Personnes vivant avec le VIH'),
        (u'perdus de vue', u'Perdus de vue'),
        (u'personnes vivant avec le vih', u'Personnes vivant avec le VIH'),
        (u'perdus de vue', u'Perdus de vue'),
        (u'consommateurs de drogues injectables', u'Consommateurs de drogues injectables'),
        (u'homme ayant des rapports avec d’autres hommes', u'Homme ayant des rapports avec d’autres hommes'),
        (u'travailleuses du sexe', u'Travailleuses du sexe'),
        (u'hommes à comportements à hauts risques', u'Hommes à comportements à hauts risques'),
        (u'clients des tds', u'Clients des TdS'),
        (u'populations migrantes', u'Populations migrantes'),
        (u'population marcérale', u'Population carcérale'),
        (u'forces armées', u'Forces armées'),
        (u'femmes enceintes', u'Femmes enceintes'),
        (u'femmes victimes de violences sexuelles', u'Femmes victimes de violences sexuelles'),
        (u'leaders religieux ou traditionnels', u'Leaders religieux ou traditionnels'),
        (u'personnels de santé', u'Personnels de santé'),
        (u'autres (cercles associatifs, cercles religieux, etc)', u'Autres (Cercles associatifs, cercles religieux, etc)'),
        (u'jeunes', u'Jeunes'),
        (u'jeunes scolarisés', u'Jeunes scolarisés'),
        (u'jeunes non-scolarisés', u'Jeunes non-scolarisés'),
        (u'orphelins et enfants vulnérables', u'Orphelins et Enfants Vulnérables'),
    )

    nom = models.CharField(max_length=40, choices=LISTE_CIBLES)
    
    class Meta:
        verbose_name_plural = "Cibles"

    madageomapping
    def __unicode__(self):
        return u"Cible : %s" % self.nom


class Organisme(models.Model):
    nom = models.CharField(max_length=40, unique=True)
    description = models.TextField( null=True)
    logo = models.ImageField(upload_to="static/media/logo/%Y/%m", blank=True, null=True)
#    status = models.ForeignKey('Status', verbose_name="Status", to_field='nom') # Un "Status" peut qualifier plrs "Organisme" et un "Organisme" ne peut avoir qu'un statut"  => Pas OneToOneField ni "OneToManyField" qui n'existe pas en Django mais ForeignKey## la class Status n'est pas encore défini, j'utilise donc le nom du modeleÃ  la place de l'objet model lui-mÃme
    referent = models.ForeignKey('self', blank=True, null=True)

    # Ainsi le model est correctement definit dans admin.
    class Meta:
        verbose_name = 'Organisme'
        verbose_name_plural = "Organismes"
        ordering = ['nom']

    # Retourne la chaîne de caractère définissant le modèle.
    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
        return u"Organisme: %s" % self.nom

    # Retourne un court descriptif
    def short(self):
        return u"%s - %s" % (self.Status, self.nom)
    short.allow_tags = True



   
class Utilisateur(models.Model):
#    user = models.OneToOneField(User, to_field='username') # La liaison OneToOne vers le modèle User (mail-nom-prenom-password)
#    photo = models.ImageField(upload_to="static/media/photos/%Y/%m", blank=True, null=True)
    user = models.OneToOneField(User) # La liaison OneToOne vers le modèle User (mail-nom-prenom-password)
    photo = models.ImageField(blank=True, null=True, upload_to="media/photos/%Y/%m")
#    organisme = models.ForeignKey('Organisme') # Va servir plus tard de groupe pour inclure les "users"
    is_responsable = models.BooleanField("Responsable autorisé à éditer la fiche", default=False)

    class Meta:madageomapping
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ['user']

    def __unicode__(self):
        return u"User: %s" % self.user.username

    def appartenance(self):
        "Returns the Organisme and person's full name."
        return u"%s %s : %s" % (self.first_name, self.last_name, self.Organisme)
    appartenance.allow_tags = True
    affiliation = property(appartenance)




# TYPE D'INTERVENTION
class Typeintervention(models.Model):
    TYPE= (
        (u'plaidoyer', u'Plaidoyer'),
        (u'ccc', u'CCC'),
        (u'promotion de préservatifs', u'Promotion de préservatifs'),
        (u'communication de masse', u'Communication de masse'),
        (u'prise en charge IST', u'Prise en chamadageomappingrge IST'),
        (u'prise en charge médicale', u'Prise en charge médicale'),
        (u'soutien', u'Soutien'),
        (u'coordination', u'Coordination'),
        (u'renforcement de capacités', u'Renforcement de capacités'),
    )

    nom = models.CharField(max_length=40, choices=TYPE)

    class Meta:
        verbose_name_plural = "Types d'intervention"

    def __unicode__(self):
        return u"Type d'intervention : %s" % self.nom



class Action(models.Model):
    titre = models.CharField(max_length = 100, verbose_name="Titre de l'action")
#    Organisme = models.ForeignKey(Organisme, verbose_name="Organisme maitre d'oeuvre", to_field='nom')
    organisme = models.ForeignKey(Organisme, verbose_name="organisme maitre d'oeuvre")
#    typeintervention = models.ManyToManyField('Typeintervention', verbose_name="Types d'intervention") 
#    typeintervention = models.ForeignKey('Typeintervention', verbose_name="Types d'intervention") 
#    cible = models.ManyToManyField('Cible', vemadageomappingrbose_name="Cibles")
    
    date_debut = models.DateField("Date de démarrage", auto_now_add=False, auto_now=False)
    date_fin = models.DateField("Date de fin", auto_now_add=False, auto_now=False)
    duree = models.CharField(max_length=40, blank=True, null=True,verbose_name="Durée de l'action")
    avancement = models.CharField( max_length=10,choices=AVANCEMENT, default='En cours',verbose_name="Etat d'avancement") 
#    createur = models.ForeignKey(Utilisateur, limit_choices_to={'is_responsable': True}, verbose_name="nom du responsable de la fiche",to_field='user')
    createur = models.ForeignKey(Utilisateur,  verbose_name="Nom du responsable de la fiche")
    description = models.TextField(null=True,  verbose_name="Description de l'action")
    commentaire = models.TextField(null=True, vmadageomappingerbose_name="Observations sur l'action")

    montant_prevu = models.PositiveIntegerField(null=True, verbose_name="Montant prévu")
    montant_disponible = models.PositiveIntegerField(null=True, verbose_name="Montant disponible")
    devise = models.CharField(max_length=10,chomadageomappingices=DEVISE, default='EUR')
    bailleurfond = models.CharField(max_length = 100,blank=True, null=True, verbose_name="Bailleurs de fond")
    origine = models.CharField(max_length = 100,verbose_name="Origine de la donnée")
    contact = models.EmailField(max_length = 100,verbose_name="Mail du contact à l'origine de la donnée")
    echelle_localisation = models.CharField(max_length=10,choices=ECHELLE_LOCALISATION, default='Nationale')
    
    operateur = models.CharField(max_length = 100, verbose_name="Opérateur en lien avec l'action")
    resultat_cf_annee_ant = models.CharField(max_length = 100,verbose_name="Résultat par rapport à l'année précédente")
    priorite_psn = models.CharField(max_length = 100,verbose_name="Priorité du PSN que l'activité appuie")

    creation = models.DateTimeField("Date de création fiche", auto_now_add=True)
    maj = models.DateTimeField("Date de la dernière mise à jour fiche", auto_now_add=True)
    login_maj = models.DateTimeField("Date de la dernière connection à la fiche action", auto_now_add=True)
#    geom = gismodels.PointField(srid=3857,default='SRID=3857;POINT(0.0 0.0)')

#    objects = gismodels.GeoManager()
     
    class Meta:
        verbose_name = "Action"
        verbose_name_plural = "Actions"madageomapping
        ordering = ['-creation']
        
    def __unicode__(self):
        return u"Action: %s" % self.titre

    # Retourne un rapide descriptif
    def short(self):
        return u"%s - %s\n%s - %s" % (self.titre, self.date.strftime("%b %d, %I:%M %p"), self.Avancement)
    short.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.creation = now()
        self.maj = now()
        super(Action, self).save(*args, **kwargs)

    # Controle de l'ancienneté de la fiche
    #def control_obsolescence(self):
    #    "Returns Action's obsolescence record Status."
    #Vérifier si le Status actuel d'Avancement n'est pas "Terminé" et que la date de "maj" est supérieur à 1 an..


# ActionCible
class ActionCible(models.Model):
    
    action = models.ForeignKey(Action)
    cible = models.ForeignKey(Cible)
    
    class Meta:
        verbose_name_plural = "Cibles"

    def __unicode__(self):
        return u"Cible : %s" % self.nom

# ActionTypeintervention
class ActionTypeintervention(models.Model):

    action = models.ForeignKey(Action)
    Typeintervention = models.ForeignKey(Typeintervention)
    objectif = models.PositiveIntegerField(null=True, verbose_name="Nombre de personnes visé")

    

    class Meta:
        verbose_name_plural = "Types d'intervention"

    def __unicode__(self):
        return u"Type d'intervention : %s" % self.nom

# Actionlocalisation
class ActionLocalisation(models.Model):

    action = models.ForeignKey(Action)
    region_status =  models.SmallIntegerField(choices=REGION_STATUS, default=0, verbose_name="Action intra Antananarivo ?")
    region = models.CharField(max_length = 50,blank=True, null=True,verbose_name="Région")
    commune = models.CharField(max_length = 50,blank=True, null=True,verbose_name="Commune")
    fokontany = models.CharField(max_length = 50,blank=True, null=True,verbose_name="Fokontany")
    latitude = models.CharField(max_length = 50,blank=True, null=True,verbose_name="latitude")
    longitude = models.CharField(max_length = 50,blank=True, null=True,verbose_name="Longitude")
    def bascule(self):
       print "aaaaaaaaaa",self.region_status
       if self.region_status == 1:
           readonly_fields=('fokontany', )
           
       else:
           readonly_fields=('region', )
           
        
     
    

    class Meta:
        verbose_name_plural = "Localisation"

    def __unicode__(self):
        return u"Localisation : %s" % self.nom
