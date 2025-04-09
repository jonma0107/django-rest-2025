from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from watchlist_app.models import Review, WatchList

from watchlist_app.serializers.review_serializer import ReviewSerializer, ReviewCreateSerializer

from watchlist_app.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly


"""
vista basada en clases utilzando mixins - las clases mixin proporcionan las acciones .list() y .create().
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
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(review_user=review_user, watchlist=watchlist)

        if review_queryset.exists():
            raise ValidationError("Ya has creado una review para esta película")

        serializer.save(watchlist=watchlist, review_user=review_user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Review creada exitosamente", "data": response.data},
            status=status.HTTP_201_CREATED
        )

    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]

    def get_queryset(self):
        watchlist_pk = self.kwargs['watchlist_pk']
        return Review.objects.filter(watchlist=watchlist_pk)
