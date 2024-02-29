from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
import os
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import Q
# from django.contrib.auth import get_user_model

# User = get_user_model()
from .models import UserBuy, ItemPhoto
from .serializers import UserCreateSerializer, UserSerializer, UserBuySerializerView,ItemPhotoSerializerCreate, ItemPhotoSerializerView
class RegisterView(APIView):
 
    def post(self, request):
        data = request.data
        serializer = UserCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)
        return Response(user.data , status=status.HTTP_201_CREATED)

class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user = UserSerializer(user)
        return Response(user.data, status=status.HTTP_200_OK)

class ItemsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = ItemPhotoSerializerCreate(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_photo_instance = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get(self, request):
        pole = request.query_params.get('pole')
        eq = request.query_params.get('equals')
        eqin = request.query_params.get('in')
        if eq:
            if pole in [field.name for field in ItemPhoto._meta.get_fields()]:
                filtered_items = ItemPhoto.objects.filter(**{f'{pole}': eq}).order_by(pole)
                serializer = ItemPhotoSerializerView(filtered_items, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                sorted_items = ItemPhoto.objects.order_by(eq)
                serializer = ItemPhotoSerializerView(sorted_items, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
        elif eqin:
            if pole in [field.name for field in ItemPhoto._meta.get_fields()]:
                filtered_items = ItemPhoto.objects.filter(**{f'{pole}__icontains': eqin}).order_by(pole)
                serializer = ItemPhotoSerializerView(filtered_items, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                filtered_items = ItemPhoto.objects.filter(Q(sort_by__icontains=eqin))
            
                serializer = ItemPhotoSerializerView(filtered_items, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
        elif pole:
            if pole in [field.name for field in ItemPhoto._meta.get_fields()]:
                unique_values = ItemPhoto.objects.values_list(pole, flat=True).distinct()
            
                return Response(list(unique_values), status=status.HTTP_200_OK)
        else:
            all_items = ItemPhoto.objects.all()
            serializer = ItemPhotoSerializerView(all_items, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)


# class ItemsView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request):
#         serializer = UserPhotosResultSerializerView(user_result_photos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)




class UserBuyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        data = request.data
        serializer = UserBuySerializerView(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        user_photo_instance = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        pole = request.query_params.get('pole')
        eq = request.query_params.get('equals')
        if eq:
            if pole in [field.name for field in UserBuy._meta.get_fields()]:
                filtered_items = UserBuy.objects.filter(**{pole: eq})
                print(filtered_items)
                serializer = UserBuySerializerView(filtered_items, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

    
    def delete(self, request, format=None):
        user_name = request.data.get('user_name')
        item = request.data.get('item')
        
        user_photos = UserBuy.objects.filter(
            user_name= user_name,
            item=item,
        )
        
        if user_photos.exists():
            for photo in user_photos:
                if os.path.exists(photo.user_photo.path):
                    os.remove(photo.user_photo.path)
            user_photos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)