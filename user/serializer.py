from rest_framework import serializers
from user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= "__all__"
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        email = instance.email
        user = super().update(instance, validated_data)
        password = validated_data.get('password')
        if password:
            user.set_password(password)
            user.save()
        return user
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token