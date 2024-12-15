import django_filters
from .models import PerfumeDetails


class PerfumeFilter(django_filters.FilterSet):
    class Meta:
        model = PerfumeDetails
        fields=['name','category','price']