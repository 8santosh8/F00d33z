from rest_framework import serializers
from Hotel.models import RestaurantLog,RestaurantItems
from payments.models import Orders

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantLog
        fields = [
            'name',
            'address',
            'street',
            'city',
            'pincode',
            'phone',
            'restimage',
        ]

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantItems
        fields = [
            'foodname',
            'type',
            'category',
            'price',
            'availability',
            'foodimage',
        ]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [
            'foodname',
            'quantity',
            'price',
            'date',
        ]
