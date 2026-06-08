from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Categoria, Producto
from .serializers import (
    CategoriaSerializer,
    ProductoSerializer
)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_permissions(self):
        if self.action in ['create', 'update',
                           'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-creado')
    serializer_class = ProductoSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['categoria']
    search_fields = ['nombre']
    ordering_fields = ['precio', 'stock', 'creado']

    def get_permissions(self):
        if self.action in ['create', 'update',
                           'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]