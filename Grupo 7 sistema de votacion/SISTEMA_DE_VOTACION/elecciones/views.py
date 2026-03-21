from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Eleccion
from .forms import EleccionForm

class EleccionListView(ListView):
    model = Eleccion
    template_name = 'elecciones/eleccion_list.html'
    context_object_name = 'elecciones'

class EleccionDetailView(DetailView):
    model = Eleccion
    template_name = 'elecciones/eleccion_detail.html'
    context_object_name = 'eleccion'

class EleccionCreateView(CreateView):
    model = Eleccion
    form_class = EleccionForm
    template_name = 'elecciones/eleccion_form.html'
    success_url = reverse_lazy('eleccion-list')
    def form_valid(self, form):
        messages.success(self.request, '✅ Elección creada.')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Nueva Elección'
        ctx['boton']  = 'Crear'
        return ctx

class EleccionUpdateView(UpdateView):
    model = Eleccion
    form_class = EleccionForm
    template_name = 'elecciones/eleccion_form.html'
    success_url = reverse_lazy('eleccion-list')
    def form_valid(self, form):
        messages.success(self.request, '✏️ Elección actualizada.')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = f'Editar: {self.object.nombre}'
        ctx['boton']  = 'Guardar Cambios'
        return ctx

class EleccionDeleteView(DeleteView):
    model = Eleccion
    template_name = 'elecciones/eleccion_confirm_delete.html'
    success_url = reverse_lazy('eleccion-list')
    context_object_name = 'eleccion'
    def form_valid(self, form):
        messages.success(self.request, '🗑️ Elección eliminada.')
        return super().form_valid(form)