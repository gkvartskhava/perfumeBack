from rest_framework import serializers
from .models import PerfumeDetails

class PerfumeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfumeDetails 
        fields = "__all__"