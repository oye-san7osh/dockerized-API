import django_filters
from django.db import models
from fvb_student.models import StudentModel


class StudentFilter(django_filters.FilterSet):
    
    # exact filter match
    match_class = django_filters.NumberFilter(field_name='st_class', lookup_expr="exact")
    
    
    # range for class filter
    min_class = django_filters.NumberFilter(field_name='st_class',
                                            lookup_expr="gte")
    
    max_class = django_filters.NumberFilter(field_name='st_class',
                                            lookup_expr='lte')
    
    
    class Meta:
        model = StudentModel
        fields = ["st_class"]