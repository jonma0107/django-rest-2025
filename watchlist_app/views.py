# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all()    
#     data = {
#         "movies": movies.values()
#     }
#     print(f'DATAAA: {data}')
#     return JsonResponse(data)

# def movie_details(request, pk):
#     movie = Movie.objects.get(pk = pk)
#     data = {
#         "movie name": movie.name,
#         "movie description": movie.description,
#         "movie active": movie.active,
#         "movie id": movie.id
#     }
#     return JsonResponse(data)