from django.urls import path,include
from django.conf.urls import url

from .views import BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookingViewSet,base_name='book')


urlpatterns = [
]

urlpatterns += router.urls