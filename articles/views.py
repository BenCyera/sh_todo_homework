from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from articles.models import Todo
from articles.serializer import TodoSerializer,TodoPostSerializer


# Todo list 전체조회 / 생성
class TodoList(APIView):
    
    # Todolist 전체조회
    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    # Todo 게시글 생성
    def post(self, request):
        serializer = TodoPostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoFix(APIView):
    
    # Todo 수정
    def put(self, request, Todo_id, format=None):
        todo = get_object_or_404(Todo, id=Todo_id)
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Todo 삭제
    def delete(self, request, Todo_id, format=None):
            todo = get_object_or_404(Todo, id=Todo_id)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
