from django.urls import include, path

from .views import ItemViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'item_list',ItemViewSet)

urlpatterns = [
    path('',include(router.urls))
    # path('items/', ItemViewSet),
]

