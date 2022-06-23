from rest_framework import serializers
from blog.models import Post,Comment,Author
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id','first_name','last_name','email')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    class Meta:
        model = Author
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.user.full_name',read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','overview','content','author','thumbnail')