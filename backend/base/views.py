from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .products import products

# Create your views here.

@api_view(['GET'])
def get_routes(request):
    routes = [
        'products/',
        'products/create',

        'products/upload',

        'products/top'

        'products/<id>',
        'products/<id>/reviews',
        
        'products/delete/<id>'
        'products/<update>/<id>'
    ]
    return Response(routes)


@api_view(['GET'])
def get_products(request):
    return Response(products)


@api_view(['GET'])
def get_product(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break
    return Response(product)