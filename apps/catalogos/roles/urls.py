from django.urls import path
from .views import RolesView


urlpatterns = [
    path('', RolesView.as_view(), ),
    path('<int:pk>', RolesView.as_view(), ),
]