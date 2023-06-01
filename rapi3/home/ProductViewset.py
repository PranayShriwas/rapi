from rest_framework import viewsets
from .ProductSerializer import ProductSerializer
from .models import *


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
