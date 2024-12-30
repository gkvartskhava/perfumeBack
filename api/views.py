from django.shortcuts import render
from .models import PerfumeDetails
from .serializers import PerfumeDetailSerializer
from rest_framework import viewsets
from .filters import PerfumeFilter
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ItemViewSet(viewsets.ModelViewSet):
    queryset = PerfumeDetails.objects.all()
    serializer_class = PerfumeDetailSerializer
    filterset_class = PerfumeFilter
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['name', 'category', 'price',]

   



