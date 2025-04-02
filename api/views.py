from django.shortcuts import render
from .models import PerfumeDetails
from .serializers import PerfumeDetailSerializer
from rest_framework import viewsets
from .filters import PerfumeFilter
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

class ItemViewSet(viewsets.ModelViewSet):
    queryset = PerfumeDetails.objects.all()
    serializer_class = PerfumeDetailSerializer
    filterset_class = PerfumeFilter
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    search_fields = ['name', 'category', 'price',]

   
# class SearchViewSet(ListAPIView):
#     queryset = PerfumeDetails.objects.all()
#     serializer_class = PerfumeDetailSerializer
#     filterset_class = PerfumeFilter
#     filter_backends = [OrderingFilter, SearchFilter]
#     search_fields = ['name', 'category', 'price',]



