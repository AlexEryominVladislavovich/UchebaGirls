from django.urls import path
from . import views
# from .views import CarsAPIView, PhoneAPIView, PhoneDetailView
from .views import CarViewSet, PhoneDetailAPIViewSet, PhoneModelViewSet

urlpatterns = [
    path('cars/', CarViewSet.as_view(), name='carsList'),
    path('phones/', PhoneModelViewSet.as_view(), name='phonesList'),
    path('phones/<int:pk>/', PhoneDetailAPIViewSet.as_view(), name='phone_detail')
]