from django.urls import path, include
from . import views
from CarritoApp.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
from django.contrib import admin


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('inicio', views.base, name='base'),
    path('index', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('Checkout', views.Checkout, name='Checkout'),
    path('faq', views.faq, name='faq'),
    path('galeria', views.galeria, name='galeria'),
    path('login/', views.login_view, name='login'),  # Cambiar a login_view para evitar conflicto
    path('logout/', views.logout_view, name='logout'),  # Cambiar a logout_view para evitar conflicto
    path('registrar/', views.register, name='registera'),
    path('regvacante', views.regvacante, name='regvacante'),
    path('crud', views.crud, name='crud'),
    path('vehiculosAdd', views.vehiculosAdd, name='vehiculosAdd'),
    path('vehiculos_del/<str:pk>', views.vehiculos_del, name='vehiculos_del'),
    path('vehiculos_findEdit/<str:pk>', views.vehiculos_findEdit, name='vehiculos_findEdit'),
    path('crud_Mecanicos', views.crud_mecanicos, name='crud_Mecanicos'),
    path('mecanico_add', views.mecanico_add, name='mecanico_add'),
    path('mecanico_del/<str:pk>', views.mecanico_del, name='mecanico_del'),
    path('mecanico_edit/<str:pk>', views.mecanico_edit, name='mecanico_edit'),
    path('admin/', admin.site.urls),
    path('', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    
]



# Se elimino:     path('vehiculosUpdate/<str:pk>', views.vehiculosUpdate, name='vehiculosUpdate'),
# Por temas de edición en el CRUD.