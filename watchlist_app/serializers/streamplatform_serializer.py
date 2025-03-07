from rest_framework import serializers
from watchlist_app.models.watchmate import StreamPlatform
from watchlist_app.serializers.watchlist_serializer import WatchListSerializer


class StreamPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many = True, read_only = True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        