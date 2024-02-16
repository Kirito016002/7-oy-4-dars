from . import serializers
from main import models

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_product(request):
    products = models.Product.objects.all()
    serializer = serializers.ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_category(request):
    categorys = models.Category.objects.all()
    serializer = serializers.CategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_enter_product(request):
    products = models.EnterProduct.objects.all()
    serializer = serializers.EnterProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_product_image(request):
    product_image = models.ProductImage.objects.all()
    serializer = serializers.ProductImageSerializer(product_image, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_wishlist(request):
    wishlists = models.WishList.objects.all()
    serializer = serializers.WishListSerializer(wishlists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_product_review(request):
    product_reviews = models.ProductReview.objects.all()
    serializer = serializers.ProductReviewSerializer(product_reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_cart(request):
    carts = models.Cart.objects.all()
    serializer = serializers.CartSerializer(carts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_cart_product(request):
    cart_products = models.CartProduct.objects.all()
    serializer = serializers.CartProductSerializer(cart_products, many=True)
    return Response(serializer.data)