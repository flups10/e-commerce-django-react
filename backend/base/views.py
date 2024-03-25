from typing import Any, Dict
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product

from .serializer import ProdcutSerializer, UserSerializer, UserSerializerWithToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Payload Data\ Decoded Coockie
        token['name'] = user.username
        token['test'] = 'hello world'

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        # Token Obtain Pair Response
        serializer = UserSerializerWithToken(self.user).data

        for key, value in serializer.items():
            data[key] = value
        
        return data
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


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