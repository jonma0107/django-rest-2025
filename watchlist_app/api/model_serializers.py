from rest_framework import serializers
from watchlist_app.api.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id']
        # exclude = ['name', 'active']

    def get_len_name(self, object):
        return len(object.name)    

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
