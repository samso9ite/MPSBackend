from rest_framework import serializers
from .models import *

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('order_id',)

class testimonialSerializer(serializers.ModelSerializer):
    testimony = serializers.CharField() 
    class Meta:
        model = Testimonial
        fields = ('testimony',)

class rateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('__all__')