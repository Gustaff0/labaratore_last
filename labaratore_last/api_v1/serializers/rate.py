from rest_framework import serializers
from webapp.models import QuoteRating

class QuoteRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteRating
        fields = ['id', 'user', 'quote']
        read_only_fields = ['id']