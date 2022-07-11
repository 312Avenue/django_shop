# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.generics import (ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView)
# from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import (ModelViewSet)
from rest_framework.filters import SearchFilter
from rest_framework import permissions

from products.filters import ProductPriceFilter
from .models import Comment, Product
from .serializers import CommentSerializer, ProductSerializer, ProductListSerializer
from .permissions import IsAuthor


# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# class ProductListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

    
# Не правильная реализация
""" class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer """


"""  """
# class ProductListCreateView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
"""  """


# Не правильная реализация
""" class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer """
    

"""  """
# class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
"""  """

# TODO: проверка прав (создавать, редактировать и удалять продукты могут только админы)
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filterset_fields = ['category', 'price']
    filterset_class = ProductPriceFilter
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return super().get_serializer_class()
        
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()


# post -> 'create'
# get -> 'list', 'retrieve'
# put -> 'update'
# patch -> 'partial_update'
# delete -> 'destroy'





#TODO: Пройтись по всему проекту, проверить все запросы
#TODO: Подготовить проект к деплою
#TODO: Написать тесты


#TODO: FastAPI
#TODO: Docker
#TODO: Async
#TODO: pytest