from userApp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'order', OrderViewset),
router.register(r'rate', RateViewSet),
router.register(r'testimonial', TestimonialViewSet)

urlpatterns = router.urls