from django.db import models

# Create your models here.
class basicInfo(models.Model):
    name   = models.CharField(max_length=80)
    date_create  = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CommonInfoPers(basicInfo):
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    gps_pos = models.URLField()

    class Meta:
        abstract = True


class Societe(CommonInfoPers):
    name   = models.CharField(max_length=80, unique= True)
    activite = models.TextField()
    contrat = models.TextField(help_text="decripe the accord with the company")
    imatriculation = models.CharField(max_length=100, unique=True)
    siege_social = models.CharField(max_length=50)
    TYPE_SOCIETES = (
        ('fournisseur', 'Fournisseur'),
        ('prestataire', 'Prestataire'),
        ('ONG', 'Donnateur'),
    )
    type_societe = models.CharField(max_length=13, choices=TYPE_SOCIETES,
                                  help_text="choose if your are personne or company")

    class Meta:
        ordering = ['type_societe', 'name']
        verbose_name_plural = "societes"


    def __str__(self):
        return '%s' ': ' '%s' % (self.name, self.type_societe) 


class Person(CommonInfoPers):
    prenom = models.CharField(max_length= 80)
    fonction_person = models.CharField(max_length=100)
    salaire  = models.FloatField()
    residence = models.CharField(max_length= 80)
    date_birth = models.DateField(auto_now_add=False)
    nom_societe = models.ForeignKey(Societe, on_delete= models.CASCADE,
                                    related_name="societes",
                                    related_query_name="societe",)
    TYPE_CONTRAT = (
        ('cdd', 'CDD' ),
        ('cdi', 'CDI'),
        ('partiel', 'INTERIME'),
    )
    type_contract = models.CharField(max_length=8, choices= TYPE_CONTRAT,
                                  help_text="choose type of contrat")

    class Meta:
        ordering = ['type_contract', 'name']
        verbose_name_plural = "persons"

    def __str__(self):
        return '%s %s' % (self.name, self.prenom)

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.name, self.prenom)
    

class basicInfoMat(basicInfo):
    price   =  models.IntegerField(null=False) 
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class CommonInfoMat(basicInfoMat):
    model   =  models.CharField(max_length=100)
    add_qte =  models.IntegerField(null=False)
    sub_qte =  models.IntegerField(null=False)

    class Meta:
        abstract = True


class Machine(CommonInfoMat):
    serial_number = models.CharField(max_length=100)
    garantie = models.DurationField()
    prev_oper_time = models.IntegerField(help_text="Previous Time of operation in mouth")
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
    type_operation = models.CharField(max_length=12, choices = TYPES_OPERATION)
    state_machine =  models.BooleanField(blank =True, default=True)
    task_describe = models.TextField()
    dat_on_oper = models.DateTimeField()
    dat_off_oper = models.DateTimeField()
    dat_next_oper = models.DateTimeField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)


