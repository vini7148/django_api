from rest_framework import serializers
from .models import course

class courseserializer(serializers.ModelSerializer):
	class Meta:
		model = course
		fields = ('id', 'name', 'language', 'price')