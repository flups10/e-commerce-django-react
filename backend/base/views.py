from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product

from .serializer import ProdcutSerializer

# Create your views here.

@api_view(['GET'])
def get_routes(request):
    routes = [
        'products/',
        'products/create',

        'products/upload',

        'products/top'

        'product/<id>',
        'product/<id>/reviews',
        
        'products/delete/<id>'
        'products/<update>/<id>'
    ]
    return Response(routes)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProdcutSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProdcutSerializer(product, many=False)
    return Response(serializer.data)