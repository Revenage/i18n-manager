from rest_framework.routers import SimpleRouter

from .views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register("", UserViewSet, base_name="user")
urlpatterns = router.urls
