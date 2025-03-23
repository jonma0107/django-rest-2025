from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from watchlist_app.models import Review, WatchList

from watchlist_app.serializers.review_serializer import ReviewSerializer, ReviewCreateSerializer


"""
vista basada en clases utilzando mixins - las clases mixin proporcionan las acciones ` .list()y` .create().
"""
class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

"""
vista basada en clases utilzando generics - vistas genéricas ya integradas que podemos usar para simplificar - SOBRE ESCRIBIMOS SUS MÉTODOS
"""

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']  # Obtiene el ID de la película desde la URL
        # serializer.save(watchlist_id=pk)  # Asigna el watchlist a la nueva review
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist) # Guarda la review con la película correcta
        

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs) # Llama a CreateAPIView
        return Response(
            {"message": "Review creada exitosamente", "data": response.data},
            status=status.HTTP_201_CREATED
        )

    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

