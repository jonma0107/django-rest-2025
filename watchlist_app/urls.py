from django.urls import path
from watchlist_app.api.function_based_views import movie_list, movie_details
from watchlist_app.views import WatchListView, WatchDetailView, StreamPlatformListView, StreamPlatformDetailView

urlpatterns = [
    path('list/', movie_list, name='list'),
    path('<int:pk>/', movie_details, name='movie_details'),

    path('watchlist/', WatchListView.as_view(), name='watchlist'),
    path('<int:pk>/', WatchDetailView.as_view(), name='watchlist_details'),
    path('platformlist/',StreamPlatformListView.as_view(), name='platformlist'),
    path('<int:pk>/', StreamPlatformDetailView.as_view(), name='platform_details'),
]
