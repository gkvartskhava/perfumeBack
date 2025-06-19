from rest_framework import serializers
from .models import PerfumeDetails

from rest_framework.validators import UniqueValidator



def validate_image(value):
    if "robot" in value.lower():
        raise serializers.ValidationError(f'{value} is not alowed')
    
    return value


unique_product_image = UniqueValidator(queryset=PerfumeDetails.objects.all(), lookup='iexact')