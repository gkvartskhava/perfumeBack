from django.shortcuts import render
from .models import PerfumeDetails
from .serializers import PerfumeDetailSerializer
from rest_framework import viewsets
from .filters import PerfumeFilter
from rest_framework import permissions

class ItemViewSet(viewsets.ModelViewSet):
    queryset = PerfumeDetails.objects.all()
    serializer_class = PerfumeDetailSerializer
    


    filterset_class = PerfumeFilter


