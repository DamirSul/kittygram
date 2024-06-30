# Обновлённый views.py
from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer

# Simple viewset
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

# # дженерики
# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer



# ОБЫЧНЫЕ ВЬЮХИ

# @api_view(['GET', 'POST'])
# def api_posts(request):
#     if request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def api_posts_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = PostSerializer(post)
#     return Response(serializer.data, status=status.HTTP_200_OK)




# CBV API VIEWS

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Post
# from .serializers import PostSerializer
# # Импортируйте в код всё необходимое


# class APIPost(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class APIPostDetail(APIView):
    
#     def get(self, request, pk):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def patch(self, request, pk):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, pk):
#         post = Post.objects.get(pk=pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
