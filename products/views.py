from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response 

from .serializers import ProductSerializer, CategorySerializer 
from .models import Product, Category

class LatestProductsList(APIView): 
    def get(self, request, format=None): 
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView): 
    def get_object(self, category_slug, product_slug): 
        try : 
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except : 
            return Http404

    def get(self, request, category_slug, product_slug, format=None): 
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data) 

class CategoryDetail(APIView): 
    def get_object(self, category_slug): 
        try : 
            return Category.objects.get(slug=category_slug)
        except : 
            return Http404

    def get(self, request, category_slug, format=None): 
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data) 
