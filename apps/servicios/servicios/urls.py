from django.urls import path
from .views import ProcesarServicioView, ProcesarServicioArbolView, ProcesarServicioGrafoDirigidoView

urlpatterns = [
    path('procesar-servicio/', ProcesarServicioView.as_view()),
    path('procesar-arbol/', ProcesarServicioArbolView.as_view()),
    path('procesar-grafo/', ProcesarServicioGrafoDirigidoView.as_view()),
]
