from rest_framework import serializers

from .models import Listing, Assignment
from pets.models import Pet


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['first_name', 'last_name', 'pets', 'assignment_set']
