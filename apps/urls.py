from django.urls import path, include

# esto esta mal, por cada modulo debiria haber un url, pero aqui hay varias, por ejemplo la ruta
# 'departamentos' y 'municipios' deberia tener un archivo urls.py dentro de la carpeta catalogos
urlpatterns = [
    path('departamentos/', include("apps.catalogos.departamentos.urls")),
    path('municipios/', include("apps.catalogos.municipios.urls")),
    path('tipotransportes/', include("apps.catalogos.tipotransportes.urls")),
    path('puestos/', include("apps.catalogos.puestos.urls")),
    path('vuelos/', include("apps.servicios.vuelos.urls")),
    path('transportes/', include("apps.servicios.transportes.urls")),
    path('hoteles/', include("apps.servicios.hoteles.urls"))
]