from rest_framework import serializers
from webapp.models import Quote
from api_v1.serializers import QuoteRatingSerializer

class QuoteSerializer(serializers.ModelSerializer):
    rating = QuoteRatingSerializer
    class Meta:
        model = Quote
        fields = ['id', 'text', 'name', 'email', 'rating', 'status', 'date']
        read_only_fields = ['id', 'date']
