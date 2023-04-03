from django.db import models

# Create your models here.
class basicInfo(models.Model):
    name   = models.CharField(max_length=80)
    date_create  = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CommonInfoPers(basicInfo):
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    gps_pos = models.URLField()

    class Meta:
        abstract = True


class Societe(CommonInfoPers):
    activite = models.TextField()
    contrat = models.TextField(help_text="decripe the accord with the company")
    imatriculation = models.CharField(max_length=100)
    siège_social = models.CharField(max_length=50)
    TYPE_SOCIETES = (
        ('fournisseur', 'Fournisseur'),
        ('prestataire', 'Prestataire'),
        ('ONG', 'Donnateur'),
    )
    type_societe = models.CharField(max_length=13, choices=TYPE_SOCIETES,
                                  help_text="choose if your are personne or company")

    class Meta:
        ordering = ['type_societe', 'nom']
        verbose_name_plural = "societes"


    def __str__(self):
        return '%s %s' % (self.type_societe, self.name)    


class Person(CommonInfoPers):
    prenom_person = models.CharField(max_length= 80)
    fonction_person = models.CharField(max_length=100)
    salaire  = models.FloatField()
    residance = models.URLField()
    date_birth = models.DateField(auto_now_add=False)
    nom_societe = models.ForeignKey(Societe, on_delete= models.CASCADE,
                                    limit_choices_to={'is_staff': True},
                                    related_name="societes",
                                    related_query_name="societe",)
    TYPE_CONTRAT = (
        ('cdd', 'CDD' ),
        ('cdi', 'CDI'),
        ('partiel', 'INTERIME'),
    )
    type_persons = models.CharField(max_length=8, choices= TYPE_CONTRAT,
                                  help_text="choose type of contrat")

    class Meta:
        ordering = ['type_persons', 'nom_person']
        verbose_name_plural = "persons"

    def __str__(self):
        return '%s %s' % (self.name, self.prenom_person)

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.name, self.prenom_person)
    

class basicInfoMat(basicInfo):
    price   =  models.IntegerField(MinValueValidator = 0, null=False) 
    person = models.ForeignKey(Person, on_delete=models.CASCADE,
                                related_name="persons",
                                related_query_name="person")
    
    class Meta:
        abstract = True


class CommonInfoMat(basicInfoMat):
    model   =  models.CharField(max_length=100)
    add_qte =  models.IntegerField(MinValueValidator = 0, null=False)
    sub_qte =  models.IntegerField(MinValueValidator = 0, null=False)

    class Meta:
        abstract = True


class Machine(CommonInfoMat):
    serial_number = models.CharField(max_length=100)
    garantie = models.DurationField()
    prev_oper_time = models.IntegerField(MinValueValidator= 0, 
                                        help_text="Previous Time of operation in mouth")
    dat_on_oper = models.DateField(auto_now_add=True)
    dat_off_oper = models.DateField(auto_now_add=False)


class Stock(CommonInfoMat):
    date_out = models.DateField(auto_now_add=False)

    TYPE_STOCK = (
        ('Consomable','Consomable'),
        ('piece', 'pièce rechange')
    )
    type_consomable = models.CharField(max_length=11, choices= TYPE_STOCK,
                                  help_text="choose type of stock")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE,
                                related_name="machines",
                                related_query_name="machine",)

class Operation(basicInfoMat):
    TYPES_OPERATION = (
        ('maitenance', 'Maintenance'),
        ('traitement', 'Traitement'),
    )
    type_operation = models.CharField(max_length=12, choises = TYPES_OPERATION)
    state_machine =  models.BooleanField(blank =True, default=True)
    task_describe = models.TextField()
    dat_on_oper = models.DateTimeField()
    dat_off_oper = models.DateTimeField()
    dat_next_oper = models.DataTimeField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,
                                related_name="stocs",
                                related_query_name="stock")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE,
                                related_name="machines",
                                related_query_name="machine")


