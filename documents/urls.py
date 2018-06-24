from rest_framework.routers import SimpleRouter

from .views import DocumentViewSet

router = SimpleRouter(trailing_slash=False)
router.register("", DocumentViewSet, base_name="document")
urlpatterns = router.urls
