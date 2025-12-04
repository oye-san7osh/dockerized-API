from django.urls import path
from fvb_student.views import StudentListCreate

app_name = "FunctionBasedAPI"

urlpatterns = [
    path('students/', StudentListCreate, name = 'student-show-list'),
    
]
