from rest_framework import serializers
from webapp.models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'text', 'name', 'email', 'rating', 'status', 'date']
        read_only_fields = ['id', 'date']
