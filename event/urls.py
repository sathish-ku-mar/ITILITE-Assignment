from .views import EventBookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', EventBookingViewSet,base_name='book')


urlpatterns = [
]

urlpatterns += router.urls