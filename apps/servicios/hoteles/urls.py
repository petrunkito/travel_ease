from django.urls import path
from .views import HotelesView


urlpatterns = [
    path('', HotelesView.as_view(), ),
    path('<int:pk>', HotelesView.as_view(), ),
]