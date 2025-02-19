from django.urls import path
# from watchlist_app.api.function_based_views import movie_list, movie_details
from watchlist_app.api.class_based_views import MovieListView, MovieDetailView

urlpatterns = [
    # path('list/', movie_list, name='list'),
    # path('<int:pk>/', movie_details, name='movie_details'),
    path('list/', MovieListView.as_view(), name='list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_details'),
]
