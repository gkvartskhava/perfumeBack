from django.urls import include, path

from .views import ItemViewSet,SearchViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'item_list',ItemViewSet, basename='item')
router.register(r'search', SearchViewSet,basename='search')

urlpatterns = [
    path('',include(router.urls))
    
]

