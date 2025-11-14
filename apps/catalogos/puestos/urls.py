from django.urls import path
from .views import PuestosView


urlpatterns = [
    path('', PuestosView.as_view(), ),
    path('<int:pk>', PuestosView.as_view(), ),
]