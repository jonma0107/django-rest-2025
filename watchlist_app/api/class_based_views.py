from rest_framework.response import Response
from rest_framework import status
from watchlist_app.api.models import Movie
from rest_framework.views import APIView
# from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.api.model_serializers import MovieModelSerializer

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieModelSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Se llama al serializador y se pasan los datos
        serializer = MovieModelSerializer(data=request.data) # recopila todos los datos, obteniendo los datos en forma de solicitud.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer=MovieModelSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


