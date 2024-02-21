from rest_framework import serializers
from main import models


class Category_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        
        
class Category_detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        
        
class Product_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        

class Product_images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'
        
        
class Product_detail_Serializer(serializers.ModelSerializer):
    images = Product_images_Serializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'