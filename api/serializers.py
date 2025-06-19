from rest_framework import serializers
from .models import PerfumeDetails
from .validators import validate_image, unique_product_image

class PerfumeDetailSerializer(serializers.ModelSerializer):
    image = serializers.CharField(validators=[validate_image,unique_product_image])

    class Meta:
        model = PerfumeDetails 
        fields = [
                    "name",
                   "category",
                    "price", 
                    "description",
                    "image",
                    
                  ]