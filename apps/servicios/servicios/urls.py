from django.urls import path
from .views import ProcesarServicioView, ProcesarServicioArbolView

urlpatterns = [
    path('procesar-servicio/', ProcesarServicioView.as_view()),
    path('procesar-arbol/', ProcesarServicioArbolView.as_view()),
]
