from . import serializers
from main import models

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_list(request):
    categorys = models.Category.objects.all()
    serializer = serializers.Category_list_Serializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_detail(request):
    cat_items = models.Product.objects.filter(category_id = request.data['id'])
    serializer = serializers.Category_detail_Serializer(cat_items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_list(request):
    items = models.Product.objects.all()
    serializer = serializers.Product_list_Serializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_detail(request, id):
    product = models.Product.objects.get(id = id)
    serializer = serializers.Product_detail_Serializer(product)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wishlist(request):
    try:
        if request.data['id']:
            product = models.Product.objects.get(id = request.data['id'])
            try:
                wish = models.WishList.objects.get(product = product)
                wish.delete()
                result = {'res':'Delete'}
            except:
                models.WishList.objects.create(
                    user = request.user,
                    product = product
                )
                result = {'res':'Create'}
    except:
        result = {'res':'Error'}
    return Response(result)

