from rest_framework import serializers
from watchlist_app.models.watchmate import StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        