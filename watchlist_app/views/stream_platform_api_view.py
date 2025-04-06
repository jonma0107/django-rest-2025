from rest_framework.response import Response
from rest_framework import status
from watchlist_app.models.watchmate import StreamPlatform 
from rest_framework.views import APIView
from watchlist_app.serializers.streamplatform_serializer import StreamPlatformSerializer


class StreamPlatformListView(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Se llama al serializador y se pasan los datos
        serializer = StreamPlatformSerializer(data=request.data) # recopila todos los datos, obteniendo los datos en forma de solicitud.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailView(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer=StreamPlatformSerializer(platform)
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response({"message":"La plataforma de stream no existe"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(platform, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except StreamPlatform.DoesNotExist:
            return Response({"message":"La plataforma de stream no existe"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            platform.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)    
        except StreamPlatform.DoesNotExist:
            return Response({"message":"La plataforma de stream no existe"}, status=status.HTTP_404_NOT_FOUND)


