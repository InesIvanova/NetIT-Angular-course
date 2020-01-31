from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product as ProductModel
from .serializers import ProductSerializer
from django.http import Http404

class ProductListView(APIView):
    def get(self, request):
        queryset = ProductModel.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductEditDelete(APIView):
    def get_object(self, pk):
        try:
            product = ProductModel.objects.get(pk=pk)
            return product
        except ProductModel.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(pk=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = self.get_object(pk=product_id)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = self.get_object(pk=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






















