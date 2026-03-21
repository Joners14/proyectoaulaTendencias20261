from django.urls import path
from . import views

urlpatterns = [
    path('',            views.CandidatoListView.as_view(),   name='candidato-list'),
    path('nuevo/',      views.CandidatoCreateView.as_view(), name='candidato-create'),
    path('<int:pk>/eliminar/', views.CandidatoDeleteView.as_view(), name='candidato-delete'),
]
