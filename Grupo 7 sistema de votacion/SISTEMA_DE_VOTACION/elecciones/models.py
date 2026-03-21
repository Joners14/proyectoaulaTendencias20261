from django.db import models

class Eleccion(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('activa',    'Activa'),
        ('cerrada',   'Cerrada'),
    ]

    nombre      = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField()
    estado      = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    creado_en   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"{self.nombre} ({self.get_estado_display()})"
    

