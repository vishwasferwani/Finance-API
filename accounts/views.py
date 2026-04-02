from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin
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