from django.urls import path
from .views import VuelosView


urlpatterns = [
    path('', VuelosView.as_view(), ),
    path('<int:pk>', VuelosView.as_view(), ),
]