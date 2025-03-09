from rest_framework import serializers
from watchlist_app.models.watchmate import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
