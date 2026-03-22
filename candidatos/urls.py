from rest_framework.routers import DefaultRouter
from .views import CandidatoViewSet

router = DefaultRouter()
router.register(r'candidatos', CandidatoViewSet)

urlpatterns = router.urls