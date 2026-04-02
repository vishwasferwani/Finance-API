from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Record
from .serializers import RecordSerializer
from accounts.permissions import IsAdmin, IsAnalyst,IsViewer
from django.db.models import Q

# Create your views here.

# CREATE
@api_view(['POST'])
@permission_classes([IsAdmin])
def create_record(request):

    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# READ
@api_view(['GET'])
@permission_classes([IsViewer])
def get_records(request):
    records = Record.objects.all()

    #filtering category/type/date
    category = request.GET.get('category')
    record_type = request.GET.get('type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if category:
        records = records.filter(category=category)

    if record_type:
        records = records.filter(type=record_type)

    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])

    #search feature
    search = request.GET.get('search')
    if search:
        records = records.filter(
            Q(category__icontains=search) |
            Q(note__icontains=search) |
            Q(type__icontains=search)
        )



    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)


# UPDATE
@api_view(['GET','PUT'])
@permission_classes([IsAdmin])
def update_record(request, id):
    record = get_object_or_404(Record, id=id)
    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return Response(serializer.data)
    
    serializer = RecordSerializer(record, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200)
    return Response(serializer.errors,status=400)


# DELETE
@api_view(['GET','DELETE'])
@permission_classes([IsAdmin])
def delete_record(request, id):
    record = get_object_or_404(Record, id=id)
    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return Response(serializer.data)
    record.delete()
    return Response(
    {"message": "Deleted"},
    status=status.HTTP_204_NO_CONTENT
    )