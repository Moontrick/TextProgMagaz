from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core import exceptions
import random
import string
from io import BytesIO
from PIL import Image, ImageFilter
from datetime import datetime
from .models import ItemPhoto, UserBuy
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "email", "password", "isAdmin")

    def validate(self, data):
        user = User(**data)
        password = data.get("password")
        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializers_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {"password": serializers_errors['non_field_errors']}
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            email=validated_data["email"],
            password=validated_data["password"],
            isAdmin = validated_data["isAdmin"]
        )
        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "email", "isAdmin")



class ItemPhotoSerializerView(serializers.ModelSerializer):
    class Meta:
        model = ItemPhoto
        fields = ("id",'itemPhoto', 'shortName', "Name", "arivel", "price", "sale", "color", "haracteristic")
    

class ItemPhotoSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = ItemPhoto
        fields = ('itemPhoto', 'shortName', "Name", "arivel", "price", "sale", "color", "haracteristic")
    def create(self, validated_data):

        itemPhoto = validated_data.get('itemPhoto')
        shortName = validated_data.get('shortName')
        Name = validated_data.get('Name')
        arivel = validated_data.get('arivel')
        price = validated_data.get('price')
        sale = validated_data.get('sale')
        color = validated_data.get('color')
        haracteristic = validated_data.get('haracteristic')

        
        user_photo_instance = ItemPhoto(
            itemPhoto=itemPhoto,
            shortName=shortName,
            Name=Name,
            arivel=arivel,
            price=price,
            sale=sale,
            color=color,
            haracteristic=haracteristic,
        )
        user_photo_instance.save()

        return user_photo_instance
    

class UserBuySerializerView(serializers.ModelSerializer):
    class Meta:
        model = UserBuy
        fields = ('user_name', 'item')

    def create(self, validated_data):
        user_name = validated_data.get('user_name')
        item = validated_data.get('item')
        print(user_name, item)
        
        user_photo_instance = UserBuy(
            user_name=user_name,
            item=item,
        )
        user_photo_instance.save()

        return user_photo_instance
