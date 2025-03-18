from rest_framework import mixins
from rest_framework import generics

from watchlist_app.models import Review

from watchlist_app.serializers.review_serializer import ReviewSerializer


"""
vista basada en clases utilzando mixins - las clases mixin proporcionan las acciones ` .list()y` .create().
"""
class ReviewListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

"""
vista basada en clases utilzando generics - vistas genéricas ya integradas que podemos usar para simplificar
"""
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer