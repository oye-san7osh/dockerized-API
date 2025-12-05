from django.urls import path
from fvb_student.views import StudentListCreate, StudentDetailUpdateDelete

app_name = "FunctionBasedAPI"

urlpatterns = [
    path('students/', StudentListCreate, name = 'student-show-list'),
    path('students/<int:pk>/', StudentDetailUpdateDelete, name = 'student-detail-update-delete-int'),
    #path('students/<slug:slug>/', StudentDetailUpdateDelete, name = 'student-detail-update-delete-text'),
    
    
]
