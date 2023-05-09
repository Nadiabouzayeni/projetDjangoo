from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path
from .import views
from .views import ProduitUpdateView,FournisseurUpdateView,FournisseurDeleteView,catalogue, produit_detail_2,ProduitDeleteView,CommandeUpdateView,CommandeDeleteView,ProduitAPIView,CategoryAPIView
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
 # Ici nous créons notre routeur
router = routers.SimpleRouter()
    # Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
    # afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')

    
urlpatterns = [
path('',views.index,name='index'),
path('register/',views.register, name = 'register'), 
#path('checkout/', views.checkout, name='catalogue'),
path('catalogue/', catalogue, name='catalogue'),
path('fournisseur_list/deletefournisseur/<str:nom>/', views.deletefournisseur,name='deletefournisseur'),
path('fournisseur_list/updatefournisseur/<str:nom>/', views.updatefournisseur, name='updatefournisseur'),
path('addfournisseur/', views.addfournisseur, name='addfournisseur'),
   # ...
path('addproduct/', views.addproduct, name='addproduct'),
path('addcategorie/', views.addcategorie, name='addcategorie'),
#path('categories/', views.categorie_list, name='categorie_list'),
path('addcommande/', views.addcommande, name='addcommande'),

path('search/', views.search, name='search'),
path('produit/<int:produit_id>/', views.produit_detail, name='produit_detail'),
path('produit/<int:produit_id>/', views.produit_detail_2, name='produit_detail_2'),

path('categories/', views.categorie_list, name='categorie_list'),
path('categorie/<int:categorie_id>/', views.categorie_detail, name='categorie_detail'),

path('fournisseur/<int:fournisseur_id>/', views.fournisseur_detail, name='fournisseur_detail'),
path('fournisseur_list/', views.fournisseur_list, name='fournisseur_list'),

path('commande/<int:commande_id>/', views.commande_detail, name='commande_detail'),
path('commande/', views.commande_list, name='commande_list'),

path('register/',views.register, name = 'register'), 
path('produit/<int:pk>/update/', ProduitUpdateView.as_view(), name='produit_update'),
path('produit/<int:pk>/delete/', ProduitDeleteView.as_view(), name='produit_delete'),
path('commande/<int:pk>/delete/', CommandeDeleteView.as_view(), name='commande_delete'),
    
    #path('', CommandeListView.as_view(), name='commande_list'),
    #path('<int:pk>/', CommandeDetailView.as_view(), name='commande_detail'),
    #path('add/', CommandeCreateView.as_view(), name='addcommande'),
path('<int:pk>/update/', CommandeUpdateView.as_view(), name='commande_update'),
path('<int:pk>/delete/', CommandeDeleteView.as_view(), name='commande_delete'),
    #url api
path('api/category/', CategoryAPIView.as_view()),
path('api/produits/', ProduitAPIView.as_view()),
path('api/', include(router.urls)),
   
]
