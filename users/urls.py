from rest_framework.routers import SimpleRouter

from users.views import PersonView

router = SimpleRouter()
router.register(r'persons', PersonView)
urlpatterns = router.urls
