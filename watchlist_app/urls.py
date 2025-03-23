from django.urls import path
from watchlist_app.api.function_based_views import movie_list, movie_details
from watchlist_app.views import WatchListView, WatchDetailView, StreamPlatformListView, StreamPlatformDetailView, ReviewListView, ReviewDetailView, ReviewCreateView, ReviewList

urlpatterns = [
    path('list/', movie_list, name='list'),
    path('<int:pk>/', movie_details, name='movie_details'),

    path('watchlist/', WatchListView.as_view(), name='watchlist'),
    path('watchlist/<int:pk>/', WatchDetailView.as_view(), name='watchlist_details'),

    path('platformlist/',StreamPlatformListView.as_view(), name='platformlist'),
    path('platformlist/<int:pk>/', StreamPlatformDetailView.as_view(), name='platform_details'),

    # path('reviews/', ReviewListView.as_view(), name='review-list'),
    # path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),

    path('watchlist/reviews/', ReviewList.as_view(), name='review-list'),
    path('watchlist/<int:pk>/reviews/', ReviewListView.as_view(), name='review-list'),
    path('watchlist/<int:pk>/review-create/', ReviewCreateView.as_view(), name='review-create'),
    path('watchlist/reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
