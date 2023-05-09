from django.db import models
from datetime import date
class Categorie (models.Model) :
    TYPE_CHOICES = [
        ('Al','Alimentaire'), 
        ('Mb','Meuble'),
        ('Sn','Sanitaire'),
        ('Vs','Vaisselle'),
        ('Vt','Vêtement'),
        ('Jx','Jouets'),
        ('Lg','Linge de Maison'),
        ('Bj','Bijoux'),
        ('Dc','Décor')

    ]

    name=models.CharField(max_length=50,default='Alimentaire')
    def __str__(self):
            return self.name  
#class categorie   

class Produit(models.Model) :
    TYPE_CHOICES = [
        ('em', 'emballé'),
        ('fr', 'Frais'),
        ('cs', 'Conserve')
    ]

    libellé=models.CharField(max_length=100)
    description=models.TextField(default='Non definie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    catégorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
            return f"({self.libellé}, {self.description} ,{self.prix}, {self.type},{self.catégorie},{self.Fournisseur})"
   

#class Produit    


class Fournisseur (models.Model) :
    nom	=models.CharField	(max_length=100)
    adresse	=models.TextField()	
    email=	models.EmailField	()
    telephone=	models.CharField	(max_length=8)
    def __str__(self):
            return f"({self.nom}, {self.adresse} ,{self.email}, {self.telephone})"
    

class ProduitNC (Produit) :
    Duree_garantie=models.	CharField	(max_length=100)
    def __str__(self):
            return self.Duree_garantie 
    
class Commande  (models.Model) :
    dateCde=models.	DateField	(null=True,default=date.today)
    totalCde	= models.DecimalField(max_digits=10,decimal_places=3)
    produits	=models.ManyToManyField('Produit')	
    def __str__(self):
             return f"({self.dateCde}, {self.totalCde},{self.produits} )"   
 
# Create your models here.
