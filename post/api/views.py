from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from post.models import Post
from rest_framework import status
from django.db.models import F




@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        print(posts)
        serializer = PostSerializer(instance=posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostSerializer(instance=post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['PUT'])
def add_like(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    # sade versiya
    # if request.method == 'PUT':
    #     post.likes += 1
    #     post.save()
    #     return Response(status=status.HTTP_202_ACCEPTED)
    
    
    if request.method == 'PUT':
        post.likes = F('likes') + 1
        post.save()
        post.refresh_from_db()
        serializer = PostSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)