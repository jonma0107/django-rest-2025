from django.contrib import admin
from watchlist_app.models.watchmate import WatchList
from watchlist_app.models.watchmate import StreamPlatform

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlatform)