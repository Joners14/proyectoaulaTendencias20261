from rest_framework.routers import DefaultRouter
from .views import EleccionViewSet

router = DefaultRouter()
router.register(r'', EleccionViewSet, basename='eleccion')

urlpatterns = router.urls