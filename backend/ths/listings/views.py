from rest_framework import generics

from .models import Listing
from .serializers import ListingSerializer


class ListingList(generics.ListAPIView):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

    def get(self, *args, **kwargs):
        response = super().get(*args, **kwargs)
        from django.db import connection
        print(len(connection.queries))
        return response
