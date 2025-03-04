from rest_framework.response import Response
from rest_framework import status
from watchlist_app.models.watchmate import WatchList 
from rest_framework.views import APIView
from watchlist_app.serializers.watchlist_serializer import WatchListSerializer

class WatchListView(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Se llama al serializador y se pasan los datos
        serializer = WatchListSerializer(data=request.data) # recopila todos los datos, obteniendo los datos en forma de solicitud.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class WatchDetailView(APIView):
    def get(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


