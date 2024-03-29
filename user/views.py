from django.shortcuts import get_object_or_404, render
from user.models import User
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from user.serializer import MyTokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response("get 요청")
    
    
class MyPageFix(APIView):
    permission_classes = [permissions.IsAuthenticated] # 로그인여부
    
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user: 
            serializer = UserSerializer(user, data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"수정완료!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)
        

