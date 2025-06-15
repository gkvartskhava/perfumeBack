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

from rest_framework import mixins, generics, viewsets

from .authentication import TokenAuthentication


class ItemViewSet(viewsets.ModelViewSet):


    queryset = PerfumeDetails.objects.all()
    serializer_class = PerfumeDetailSerializer
    filterset_class = PerfumeFilter
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]
    search_fields = ['name', 'category', 'price',]



class ProductMixinView(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = PerfumeDetails.objects.all()
    serializer_class = PerfumeDetailSerializer
    lookup_field = "pk"

    def get(self,request, *args, **kwargs):
        # print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


   
# class SearchViewSet(ListAPIView):
#     queryset = PerfumeDetails.objects.all()
#     serializer_class = PerfumeDetailSerializer
#     filterset_class = PerfumeFilter
#     filter_backends = [OrderingFilter, SearchFilter]
#     search_fields = ['name', 'category', 'price',]



