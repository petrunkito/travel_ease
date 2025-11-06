from django.urls import path
from .views import TransportesView


urlpatterns = [
    path('', TransportesView.as_view(), ),
    path('<int:pk>', TransportesView.as_view(), ),
]