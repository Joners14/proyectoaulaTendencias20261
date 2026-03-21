from rest_framework.routers import DefaultRouter
from .views import VotanteViewSet

router = DefaultRouter()
router.register(r'', VotanteViewSet, basename='votante')

urlpatterns = router.urls