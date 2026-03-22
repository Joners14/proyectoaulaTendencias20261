from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/elecciones/', include('elecciones.urls')),
    path('api/candidatos/', include('candidatos.urls')),
    path('api/votantes/', include('votantes.urls')),
]