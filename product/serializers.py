from rest_framework import serializers
from .models import Car, Phone, Category, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CarSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Car
        fields = ['__all__']


class PhoneSerializer(serializers.Serializer):
    namePhone = serializers.CharField(max_length=30)
    pricePhone = serializers.IntegerField()
    seria = serializers.CharField(max_length=30)
    category = CategorySerializer(many = True)

    def create(self, validate_data):
        return Phone.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.namePhone = validated_data.get('namePhone', instance.namePhone)
        instance.pricePhone = validated_data.get('pricePhone', instance.pricePhone)
        instance.seria = validated_data.get('seria', instance.seria)
        instance.save()
        return instance

    def validate_namePhone(self, value):
        value = value.strip()
        value = value.capitalize()
        valid_namePhone = ['Iphone', 'Sumsung', 'Huawei']
        if value not in valid_namePhone:
            raise serializers.ValidationError('Введите один из трёх предложенных телефонов')
        return value

    def validated_pricePhone(self, value):
        if value <= 0:
            raise serializers.ValidationError('Цена должна быть положительным числом')
        if value > 1000000:
            raise serializers.ValidationError('Цена не должна привышать 1000000')
        return value

    def validated_seria(self, value):
        value = value.strip
        value = value.upper
        if value.lenght > 30:
            raise serializers.ValidationError('Серия не должна привешать 30 символов')
        return value