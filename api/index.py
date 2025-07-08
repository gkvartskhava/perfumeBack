
from algoliasearch_django import AlgoliaIndex 
from .models import PerfumeDetails
from algoliasearch_django.decorators import register


# import algoliasearch_django as algoliasearch
# algoliasearch.register(PerfumeDetails)

  
@register(PerfumeDetails)
class PerfumeDetailsIndex(AlgoliaIndex):
    fields = ['name', 'description', 'price', 'in_stock']
    settings = {
        'searchableAttributes': ['name', 'description', 'price', 'category'],
        'attributesForFaceting': ['price', 'in_stock'],
    }