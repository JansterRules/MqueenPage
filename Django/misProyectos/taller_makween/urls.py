from django.urls import path
from . import views

urlpatterns=[
    path('', views.base, name='base'),
    path('index', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('Checkout', views.Checkout, name='Checkout'),
    path('faq', views.faq, name='faq'),
    path('galeria', views.galeria, name='galeria'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('regvacante', views.regvacante, name='regvacante'),
]