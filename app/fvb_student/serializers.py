from rest_framework import serializers
from fvb_student.models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = StudentModel
        fields = "__all__"
        