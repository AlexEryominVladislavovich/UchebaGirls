from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from .models import Car, Phone, Profile, Category
from .serializers import CarSerializer, PhoneSerializer, ProfileSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permission import AllowAny

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Profile.objectd.all()
    serializer_class = ProfileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CarAPIView(generics.ListAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # Кастомная реализация

    # def list(self, request):
    #     queryset = Cars.objects.all()
    #     serializer = CarsSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     car = get_object_or_404(Cars, pk=pk)
    #     serializer = CarsSerializer(car)
    #     return Response(serializer.data)
    #
    # def create(self, request):
    #     serializer = CarsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    #
    # def update(self, request, pk):
    #     car = get_object_or_404(Cars, pk=pk)
    #     serializer = CarsSerializer(car, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    #
    # def partial_update(self, request, pk=None):
    #     car = get_object_or_404(Cars, pk=pk)
    #     serializer = CarsSerializer(car, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    #
    # def destroy(self, request, pk):
    #     car = get_object_or_404(Cars, pk=pk)
    #     car.delete()
    #     return Response(status=204)


class PhoneModelViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneDetailAPIViewSet(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny)

    def list(self, request):
        queryset = Phone.objects.all()
        serializer = PhoneSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        phone = get_object_or_404(Phone, pk=pk)
        serializer = PhoneSerializer(phone)
        return Response(serializer.data)

    def create(self, request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk):
        queryset = Phone.objects.all()
        serializer = PhoneSerializer(queryset)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Phone.objects.all()
        serializer = PhoneSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk):
        queryset = Phone.objects.all()
        serializer = PhoneSerializer(queryset)
        return Response(serializer.data)

# Реализация через Дженерик PhoneAPIView

# class PhoneAPIView(generics.ListCreateAPIView):
#     queryset = Phone.objects.all()
#     serializer_class = PhoneSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#
# class PhoneDetailView(generics.RetrieveAPIView):
#     queryset = Phone.objects.all()
#     serializer_class = PhoneSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

# class PhonesListView(APIView):
#     def get(self, request):
#         data = 'phones: '
#         return Response(data)