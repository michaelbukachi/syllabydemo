from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer, AddProductImageSerializer
from utils.pagination import CustomPagination


# Create your views here.


class ProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddProductImage(generics.GenericAPIView):
    serializer_class = AddProductImageSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            image = request.FILES['image']
            ProductImage.objects.create(product=product, file=image)
            return JsonResponse(data={"status": "ok"})
        except KeyError:
            return JsonResponse(data={"status": "Image file not found."}, status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return JsonResponse(data={"status": "Product not found."}, status=status.HTTP_404_NOT_FOUND)


    def get_queryset(self):
        return ProductImage.objects.all()
