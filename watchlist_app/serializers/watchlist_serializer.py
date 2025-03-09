from rest_framework import serializers
from watchlist_app.models.watchmate import WatchList
from watchlist_app.serializers.review_serializer import ReviewSerializer


class WatchListSerializer(serializers.ModelSerializer):

    reviews = serializers.StringRelatedField(many = True, read_only = True)
    
    class Meta:
        model = WatchList
        fields = "__all__"        
