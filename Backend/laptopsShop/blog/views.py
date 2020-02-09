from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import User, Post, Comment
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class UserListCreate(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListCreate(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListCreate(APIView):
    def get(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEditDelete(APIView):
    def get_object(self, pk):
        try:
            product = User.objects.get(pk=pk)
            return product
        except User.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(pk=product_id)
        serializer = UserSerializer(product)
        return Response(serializer.data)

    def delete(self):
        pass


class PostEditDelete(APIView):
    def get_object(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(pk=product_id)
        serializer = PostSerializer(product)
        return Response(serializer.data)

    def delete(self, request, product_id):
        post = self.get_object(pk=product_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, product_id):
        post = self.get_object(pk=product_id)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentEditDelete(APIView):
    def get_object(self, pk):
        try:
            product = Comment.objects.get(pk=pk)
            return product
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(pk=product_id)
        serializer = CommentSerializer(product)
        return Response(serializer.data)
