from django.db import models


# Create your models here.
class utilisateur(models.Model):
    user = models.OneToOneField(User) # La liaison OneToOne vers le modèle User (mail-nom-prenom-password)
    photo = models.ImageField(blank=True, null=True, upload_to="media/photos/%Y/%m")
    is_responsable = models.BooleanField("Responsable autorisé à éditer la fiche", default=False)

    class Meta:
        verbose_name = "utilisateur"
        verbose_name_plural = "utilisateurs"
        ordering = ['user']

    def __unicode__(self):
        return u"User: %s" % self.user.username

class organisme(models.Model):
    nom = models.CharField(max_length=40)
    description = models.TextField(null=True)
    logo = models.ImageField(upload_to="media/logo/%Y/%m", null=True)
    #status = models.OneToOneField('status', verbose_name="status") # Un "status" peut qualifier un "organisme" et un "organisme" ne peut avoir qu'un statut"  => OneToOneField ## la class status n'est pas encore défini, j'utilise donc le nom du modèle la place de l'objet model lui-même

    # Ainsi le model est correctement definit dans admin.
    class Meta:
        verbose_name = 'organisme'
        verbose_name_plural = "organismes"
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
        return u"%s - %s" % (self.status, self.nom)
    short.allow_tags = True

class typeIntervention(models.Model):
    CATEGORIE = (
        (u'Plaidoyer', u'Plaidoyer'),
        (u'Promotion de préservatifs', u'Promotion de préservatifs'),
        (u'Communication de masse', u'Communication de masse'),
        (u'eau/assainissement', u'Eau/Assainissement'),
    )

    nom = models.CharField(max_length=40, choices=CATEGORIE)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u"Catégorie: %s" % self.nom

class avancement(models.Model):
    AVANCEMENT = (
        (u'en attente', u'En attente'),
        (u'initié', u'Initié'),
        (u'à mi parcours', u'A mi parcours'),
        (u'Terminé', u'Terminé'),
    )

    nom = models.CharField(max_length=40, choices=AVANCEMENT)

    class Meta:
        verbose_name_plural = "Avancements"

    def __unicode__(self):
        return u"Avancement: %s" % self.nom


class action(models.Model):
    titre = models.CharField(max_length = 100)
    date = models.DateTimeField("Date de démarrage", auto_now_add=False, auto_now=False)
    duree = models.CharField(max_length=40)
    operateur = models.CharField(max_length = 100)
    description = models.TextField(null=True)
    #region = models.OneToOneField('mdgRegion', verbose_name="région") # Ici "OneToOneField" précise qu'une "action" ne se déroule que dans une région.
    localisation = models.CharField(max_length=50)
    illustration = models.ImageField(upload_to="media/illustration/%Y/%m", null=True)
    responsable = models.ForeignKey(utilisateur, limit_choices_to={'is_responsable': True}, verbose_name="nom du responsable de la fiche")
    organisme = models.ForeignKey(organisme, verbose_name="organisme maitre d'oeuvre")
    avancement = models.ForeignKey('avancement', verbose_name="état d'avancement") # Un "avancement" peut concerner plrs "actions" mais une "action" ne peut avoir qu'un état d'"avancement" => ForeignKey
    #categories = models.ManyToManyField('categorie', verbose_name="catégorie") # Un ou plrs "catégories" peut qualifier une "action" et une "action" peut agir dans un ou plrs "catégories"  => ManyToManyField
    montant = models.PositiveIntegerField("Montant", null=True)
    creation = models.DateTimeField("Date de création fiche") #auto_now_add=True, auto_now=True)
    maj = models.DateTimeField("Date de mise à jour fiche", auto_now_add=True, auto_now=True)
    geom = models.GeometryField(srid=4326)
    
    objects = models.GeoManager()
     
    class Meta:
        verbose_name = "action"
        verbose_name_plural = "actions"
        ordering = ['-creation']
        
    def __unicode__(self):
        return u"Action: %s" % self.titre

    # Retourne un rapide descriptif
    def short(self):
        return u"%s - %s\n%s - %s" % (self.titre, self.region, self.date.strftime("%b %d, %I:%M %p"), self.avancement)
    short.allow_tags = True


