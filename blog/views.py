from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import generics, serializers, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter

from blog.serializer import PostSerializer,AuthorSerializer,PostCreateSerializer
from blog.models import Post,Author

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('title','overview','author__user__first_name')
    pagination_class = PageNumberPagination
    
class PostCreateView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostCreateSerializer

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=AuthorSerializer

class AuthorBlogListView(generics.ListAPIView):
    def get_queryset(self):
        user_id = self.kwargs['pk']
        qs = Post.objects.filter(author__user__id = user_id)
        print(user_id)
        return qs
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    
