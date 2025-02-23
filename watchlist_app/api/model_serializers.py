from rest_framework import serializers
from watchlist_app.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = "__all__"
        fields = ['id']
        # exclude = ['name', 'active']

    # Object-level Validation
    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("name and description should be different")
        else:
            return data

    # Field-level Validation
    def validate_description(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Description is too short")
        else:
            return value    
