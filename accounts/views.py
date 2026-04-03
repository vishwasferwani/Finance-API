from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer,LoginSerializer
from .permissions import IsAdmin
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.

# CREATE USER
@api_view(['POST'])
@permission_classes([IsAdmin])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# GET ALL USERS
@api_view(['GET'])
@permission_classes([IsAdmin])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# UPDATE USER
@api_view(['PUT', 'GET'])
@permission_classes([IsAdmin])
def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# DELETE USER
@api_view(['DELETE','GET'])
@permission_classes([IsAdmin])
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    user.delete()
    return Response({'message': 'User deleted'})

@api_view(['POST'])
def Login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user and user.is_active:
            login(request, user)
            return Response({"message": "Login successful"},status=200)
        else:
            return Response({"error": "Invalid credentials or inactive account"}, status=400)
    return Response(serializer.errors, status=400)
