from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('galeria',views.galeria, name='galeria'),
    path('publicacion', views.crearPublicacion, name="crearPublicacion"),
    path('form_mod_publicacion/<id>', views.form_mod_publicacion, name="form_mod_publicacion"),
    path('form_del_publicacion/<id>', views.form_del_publicacion, name="form_del_publicacion")
]