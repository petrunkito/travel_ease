from django.urls import path
from .views import TipoTransportesView


urlpatterns = [
    path('', TipoTransportesView.as_view(), ),
    path('<int:pk>', TipoTransportesView.as_view(), ),
]