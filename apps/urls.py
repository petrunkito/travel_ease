from django.urls import path, include

urlpatterns = [
    path('departamentos/', include("apps.departamentos.urls")),
    path('municipios/', include("apps.municipios.urls"))
]