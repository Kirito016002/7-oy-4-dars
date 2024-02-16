from rest_framework.serializers import ModelSerializer
from main import models


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        
        
class EnterProductSerializer(ModelSerializer):
    class Meta:
        model = models.EnterProduct
        fields = '__all__'
        
        
class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'
        
        
class WishListSerializer(ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'
        
        
class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = models.ProductReview
        fields = '__all__'
        
        
class CartSerializer(ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'
        
        
class CartProductSerializer(ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'      