from django.urls import path
from .views import UsuariosView


urlpatterns = [
    path('', UsuariosView.as_view(), ),
    path('<int:pk>', UsuariosView.as_view(), ),
]