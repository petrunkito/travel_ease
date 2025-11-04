from django.urls import path
from .views import DepartamentosView


urlpatterns = [
    path('', DepartamentosView.as_view(), ),
    path('<int:pk>', DepartamentosView.as_view(), ),
]