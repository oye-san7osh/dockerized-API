from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from fvb_student.models import StudentModel
from fvb_student.serializers import StudentSerializer
from fvb_student.paginations import StudentPagination
from fvb_student.filters import StudentFilter
from django.db.model import Q


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def StudentListCreate(request):
    
    if request.method == "GET":
        
        # without pagination
        """students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)"""
        
        
        # with pagination
        students = StudentModel.objects.all()
        
        filtered_student = StudentFilter(request.GET, queryset=students).qs
        
        search = request.query_params.get("search")
        if search:
            filtered_student = filtered_student.filter(
                Q(st_full_name__icontains=search) |
                Q(st_roll__icontains=search) |
                Q(father_name__icontains=search) |
                Q(mother_name__icontains=search) |
                Q(address__icontains=search) |
                Q(email__icontains=search) |
                Q(st_faculty__icontains=search)
                )
        
        
        ordering = request.query_params.get("ordering")
        if ordering:
            filtered_student = filtered_student.order_by(ordering)
            
            
            
        paginator = StudentPagination()
        result_page_st = paginator.paginate_queryset(filtered_student, request)
        
        serializer = StudentSerializer(result_page_st, many=True)
        return paginator.get_paginated_response(serializer.data)
        
        
    
    
    if request.method == "POST":
        
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny])
def StudentDetailUpdateDelete(request, pk):
    
    try:
        student = StudentModel.objects.get(pk=pk)
    except StudentModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    if request.method == "PUT":
        
        serializer = StudentSerializer(student, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        
        student.delete()
        return Response(status=status.HTTP_404_NO_CONTENT)
    
        