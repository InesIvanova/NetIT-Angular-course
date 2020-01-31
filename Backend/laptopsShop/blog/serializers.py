from rest_framework import serializers
from .models import Post as PostModel
from .models import User as UserModel
from .models import Comment as Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
