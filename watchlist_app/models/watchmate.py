from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name 


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0) # VALOR GLOBAL SEGÚN LAS RESEÑAS
    number_rating = models.IntegerField(default=0) # CANTIDAS DE RESEÑAS
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models. ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Rating: " + str(self.rating) + " - " + "Description: " + self.description + " - " + "User: " + str(self.review_user)
         

    