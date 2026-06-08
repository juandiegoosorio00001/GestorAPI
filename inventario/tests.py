from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Categoria, Producto


class ProductoTests(APITestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre='Tecnología',
            descripcion='Productos tecnológicos'
        )

    def test_crear_producto_valido(self):
        data = {
            "nombre": "Laptop",
            "precio": 2500,
            "stock": 5,
            "categoria": self.categoria.id
        }

        response = self.client.post(
            '/api/v1/productos/',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_precio_negativo(self):
        data = {
            "nombre": "Mouse",
            "precio": -100,
            "stock": 10,
            "categoria": self.categoria.id
        }

        response = self.client.post(
            '/api/v1/productos/',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )