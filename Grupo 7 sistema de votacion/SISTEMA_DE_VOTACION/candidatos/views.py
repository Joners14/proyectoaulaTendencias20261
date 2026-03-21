from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Candidato
from .forms import CandidatoForm

class CandidatoListView(ListView):
    model = Candidato
    template_name = 'candidatos/candidato_list.html'
    context_object_name = 'candidatos'

class CandidatoCreateView(CreateView):
    model = Candidato
    form_class = CandidatoForm
    template_name = 'candidatos/candidato_form.html'
    success_url = reverse_lazy('candidato-list')
    def form_valid(self, form):
        messages.success(self.request, '✅ Candidato creado.')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Nuevo Candidato'
        ctx['boton'] = 'Crear'
        return ctx

class CandidatoDeleteView(DeleteView):
    model = Candidato
    template_name = 'candidatos/candidato_confirm_delete.html'
    success_url = reverse_lazy('candidato-list')
    context_object_name = 'candidato'
    def form_valid(self, form):
        messages.success(self.request, '🗑️ Candidato eliminado.')
        return super().form_valid(form)