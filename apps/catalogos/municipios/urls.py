from django.urls import path
from .views import MunicipiosView


urlpatterns = [
    path('', MunicipiosView.as_view(), ),
    path('<int:pk>', MunicipiosView.as_view(), ),
]