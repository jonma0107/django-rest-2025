from rest_framework import serializers
from watchlist_app.models.watchmate import Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = Review
        fields = '__all__'
        

class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review        
        exclude = ('watchlist', 'review_user',)

