from django.shortcuts import render
from django.http import JsonResponse
from .products import products

# Create your views here.
def getRoutes(request):
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
    return JsonResponse(routes, safe=False)

def getProducts(request):

    return JsonResponse(products, safe=False)