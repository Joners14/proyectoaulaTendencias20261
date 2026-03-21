from django.urls import path
from . import views

urlpatterns = [
    path('',              views.EleccionListView.as_view(),   name='eleccion-list'),
    path('nueva/',        views.EleccionCreateView.as_view(), name='eleccion-create'),
    path('<int:pk>/',     views.EleccionDetailView.as_view(), name='eleccion-detail'),
    path('<int:pk>/editar/',   views.EleccionUpdateView.as_view(), name='eleccion-update'),
    path('<int:pk>/eliminar/', views.EleccionDeleteView.as_view(), name='eleccion-delete'),
]