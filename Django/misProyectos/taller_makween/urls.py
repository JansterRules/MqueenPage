from django.urls import path, include # Utilizar para autenticación.
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    
    path('index', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('Checkout', views.Checkout, name='Checkout'),
    path('faq', views.faq, name='faq'),
    path('galeria', views.galeria, name='galeria'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('accounts', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('regvacante', views.regvacante, name='regvacante'),
    path('crud', views.crud, name='crud'),
    path('vehiculosAdd', views.vehiculosAdd, name='vehiculosAdd'),
    path('vehiculos_del/<str:pk>', views.vehiculos_del, name='vehiculos_del'),
    path('vehiculos_findEdit/<str:pk>', views.vehiculos_findEdit, name='vehiculos_findEdit'),
    path('crud_Mecanicos', views.crud_mecanicos, name='crud_Mecanicos'),
    path('mecanico_add', views.mecanico_add, name='mecanico_add'),
    path('mecanico_del/<str:pk>', views.mecanico_del, name='mecanico_del'),
    path('mecanico_edit/<str:pk>', views.mecanico_edit, name='mecanico_edit'),
]

# Se elimino:     path('vehiculosUpdate/<str:pk>', views.vehiculosUpdate, name='vehiculosUpdate'),
# Por temas de edición en el CRUD.