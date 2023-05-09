from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer,ProduitSerializer
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from .forms import ProduitForm,CommandeForm,fournisseurForm,UserRegistrationForm,CategorieForm, fournisseurForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Produit, Categorie, Fournisseur, ProduitNC, Commande
from django.contrib.auth.forms import UserCreationForm
#from .models import Produit

# Create your views here.


@login_required(login_url="/users/login")
def index(request):
    template = loader.get_template('magasin/mesProduits.html')
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html ', context)

#catalogue................

def catalogue(request):
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/catalogue.html', context)


#categorie.......................
#list
@login_required(login_url="/users/login")
def categorie_list(request):
    template = loader.get_template('magasin/categorie_list.html')
    categories = Categorie.objects.all()
    return render(request, 'magasin/categorie_list.html', {'categories': categories})

#fournisseur............................
#details
@login_required(login_url="/users/login")
def fournisseur_detail(request, fournisseur_id):
    template = loader.get_template('magasin/fournisseur_detail.html')
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    produits = fournisseur.produit_set.all()
    context = {
        'fournisseur': fournisseur,
        'produits': produits,
    }
    return render(request,'magasin/fournisseur_detail.html', context)

#list
@login_required(login_url="/users/login")
def fournisseur_list(request):
    template = loader.get_template('magasin/fournisseur_list.html')
    fournisseurs = Fournisseur.objects.all()
    context = {
        'fournisseurs': fournisseurs
    }
    return render(request, 'magasin/fournisseur_list.html', context)

#update
def updatefournisseur(request,nom):  
    fournisseur = get_object_or_404(Fournisseur,nom=nom) 
    if request.method == 'POST':
        form = fournisseurForm(request.POST, instance=fournisseur) 
        if form.is_valid():
            form.save()
            return redirect(reverse('magasin/fournisseur_list'))
    else:
        form = fournisseurForm(instance=fournisseur)
    context = {'form': form, 'fournisseur': fournisseur}        
    return render(request,'magasin/updatefournisseur.html',context)
#delete
@login_required(login_url="/users/login")
def deletefournisseur(request,nom): 
    fournisseur = Fournisseur.objects.get(nom=nom)  
    fournisseur.delete()
    return redirect('magasin/fournisseur_list')
#Produit.......................
#details

@login_required(login_url="/users/login")
def produit_detail(request, produit_id):
    template = loader.get_template('magasin/produit_detail.html')
    produit = Produit.objects.get(id=produit_id)
    return render(request, 'magasin/produit_detail.html', {'produit': produit})

def produit_detail_2(request, produit_id):
    template = loader.get_template('magasin/produit_detail_2.html')
    produit = Produit.objects.get(id=produit_id)
    return render(request, 'magasin/produit_detail_2.html', {'produit': produit})

#commande
@login_required(login_url="/users/login")
def commande_detail(request, commande_id):
    template = loader.get_template('magasin/commande_detail.html')
    commande = Commande.objects.get(id=commande_id)
    produits = commande.produits.all()
    context = {
        'commande': commande,
        'produits': produits,
    }    
    return render(request, 'magasin/commande_detail.html', context)

@login_required(login_url="/users/login")
def commande_list(request):
    template = loader.get_template('magasin/commande_list.html')
    commandes = Commande.objects.all()
    context = {
        'commandes': commandes
    }
    return render(request, 'magasin/commande_list.html', context)


def search(request):
    template = loader.get_template('magasin/search.html')
    query = request.GET.get('q')
    if query:
        produits = Produit.objects.filter(
            Q(libelle__icontains=query) | Q(description__icontains=query)
        )
        categories = Categorie.objects.filter(name__icontains=query)
        context = {
            'produits': produits,
            'categories': categories,
            'query': query  # pass the query to the context
        }
    else:
        context = {
            'produits': None,
            'categories': None,
            'query': None
        }
    return render(request, 'magasin/search.html', context)

@login_required(login_url="/users/login")
def categorie_detail(request, categorie_id):
    template = loader.get_template('magasin/categorie_detail.html')
    # Retrieve the category object with the specified ID or return a 404 error
    categorie = Categorie.objects.get(id=categorie_id)
    # Retrieve all the products that belong to the specified category
    produits = categorie.produit_set.all()
    context = {
        'categorie': categorie,
        'produits': produits,
    }
    return render(request, 'magasin/categorie_detail.html', context)


@login_required(login_url="/users/login")
def addproduct(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide
    return render(request,'magasin/majProduits.html',{'form':form})


@login_required(login_url="/users/login")
def addcategorie(request):
    if request.method == "POST" :
        form = CategorieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin/categories')
    else :
        form = CategorieForm() #créer formulaire vide
    return render(request, 'magasin/majcategorie.html', {'form': form})


def addcommande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/commande')
    else:
        date_cde = request.GET.get('date')
        total_cde = request.GET.get('total')
        produit_id = request.GET.get('produit')
        produit = Produit.objects.get(id=produit_id)
        initial_data = {
            'dateCde': date.today(), 
            'totalCde': total_cde,
            'produits': [produit],
        }
        form = CommandeForm(initial=initial_data)
    return render(request, 'magasin/majCommande.html', {'form': form})



@login_required(login_url="/users/login")
def addfournisseur(request):
    if request.method == "POST" :
        form = fournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/fournisseur')
    else :
        form = fournisseurForm() #créer formulaire vide
    return render(request,'magasin/majfournisseurs.html',{'form':form})


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    return render(request, 'registration/register.html', {'form': form})

class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'magasin/produit_update.html'
    success_url = reverse_lazy('index')
class FournisseurUpdateView(UpdateView):
    model = Fournisseur
    form_class = fournisseurForm
    template_name = 'magasin/updatefournisseur.html'
    success_url = reverse_lazy('index')


class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'magasin/produit_confirm_delete.html'
    success_url = reverse_lazy('index')
class FournisseurDeleteView(DeleteView):
    model = Fournisseur
    template_name = 'magasin/deletefournisseur.html'
    success_url = reverse_lazy('index')

class CommandeUpdateView(UpdateView):
    model = Commande
    form_class = CommandeForm
    template_name = 'majCommande.html'
    

class CommandeDeleteView(DeleteView):
    model = Commande
    success_url = reverse_lazy('commande_list')
def register(request):
     if request.method == 'POST' :
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=password)
               login(request,user)
               messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
               return redirect('home')
     else :
          form = UserCreationForm()
     return render(request,'registration/register.html',{'form' : form})

def commande_delete(request, pk):
    commande = get_object_or_404(Commande, pk=pk)

    if request.method == 'POST':
        commande.delete()
        return redirect('commande_list')

    context = {'commande': commande}
    return render(request, 'commande_delete.html', context)

class CategoryAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class ProduitAPIView(APIView):
 
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)


class ProductViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
