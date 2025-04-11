from django.urls import path, include
# from .views import CarsAPIView, PhoneAPIView, PhoneDetailView
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, PhoneModelViewSet, PhoneDetailAPIViewSet, CategoryViewSet, RegistrationViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'car',  CarViewSet, basename='car')
router.register(r'phone', PhoneModelViewSet, basename='phone')
router.register(r'profile', RegistrationViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls))
]

# Стандартный urlpatterns без роутеров
# urlpatterns = [
#     path('cars/', CarViewSet.as_view(), name='carsList'),
#     path('phones/', PhoneModelViewSet.as_view(), name='phonesList'),
#     path('phones/<int:pk>/', PhoneDetailAPIViewSet.as_view(), name='phone_detail')
# ]