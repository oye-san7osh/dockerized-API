from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from fvb_student.models import StudentModel
from fvb_student.serializers import StudentSerializer
from fvb_student.paginations import StudentPagination



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
        
        paginator = StudentPagination()
        result_page_st = paginator.paginate_queryset(students, request)
        
        serializer = StudentSerializer(result_page_st, many=True)
        return paginator.get_paginated_response(serializer.data)
        
        
    
    
    if request.method == "POST":
        
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

