from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.models import Product

from base.serializer import ProdcutSerializer

from rest_framework import status


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProdcutSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', "POST"])
def get_product(request):
    product = Product.objects.get(_id=request.data["pk"])
    serializer = ProdcutSerializer(product, many=False)
    return Response(serializer.data)