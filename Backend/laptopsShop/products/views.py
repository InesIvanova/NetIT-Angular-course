from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product as ProductModel
from .serializers import ProductSerializer


class ProductListView(APIView):
    def get(self, request):
        queryset = ProductModel.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
