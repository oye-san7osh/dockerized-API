import django_filters
from django.db import models
from datetime import date, timedelta
from fvb_student.models import StudentModel


class StudentFilter(django_filters.FilterSet):
    
    # exact filter match
    match_class = django_filters.NumberFilter(field_name='st_class', lookup_expr="exact")
    
    
    # range for class filter
    min_class = django_filters.NumberFilter(field_name='st_class',
                                            lookup_expr="gte")
    
    max_class = django_filters.NumberFilter(field_name='st_class',
                                            lookup_expr='lte')
    
    # by faculty
    match_faculty = django_filters.CharFilter(field_name="st_faculty", lookup_expr="iexact")
    
    # by gender
    match_gender = django_filters.CharFilter(field_name="gender", lookup_expr="exact")
    
    # by active status
    is_active = django_filters.BooleanFilter(field_name='is_active', lookup_expr="exact")
    
    
    # by age/date of birth
    match_dob = django_filters.DateFilter(field_name="date_of_birth", lookup_expr="exact")
    
    
    # by range of age/date of birth
    min_dob = django_filters.DateFilter(field_name="date_of_birth", lookup_expr="gte")
    max_dob = django_filters.DateFilter(field_name="date_of_birth", lookup_expr="lte")
    
    
    # by admission date
        # year
    admission_year = django_filters.NumberFilter(field_name="admission_date", lookup_expr="year")

        # month
    admission_month = django_filters.NumberFilter(field_name="admission_date", lookup_expr="month")
    
    
    # recent N days
    recent_days = django_filters.NumberFilter(method="filter_by_recent")
    
    def filter_by_recent(self, queryset, name, value):
        value = int(value)  # convert Decimal to int
        recent = date.today() - timedelta(days=value)
        return queryset.filter(admission_date__gte=recent)
    
    
    # old admission (older than N days)
    old_days = django_filters.NumberFilter(method="filter_by_old")
    
    def filter_by_old(self, queryset, name, value):
        value = int(value)  # convert Decimal to int
        cutoff = date.today() - timedelta(days=value)
        return queryset.filter(admission_date__lte=cutoff)
    
    
    # by location
    address_detail = django_filters.CharFilter(field_name="address", lookup_expr="icontains")
    
    
    # by parent detail
    father_contain = django_filters.CharFilter(field_name="father_name", lookup_expr="icontains")
    cont_num = django_filters.NumberFilter(field_name="guardian_contact", lookup_expr="exact")
    
    
    # by roll number
    roll_start = django_filters.CharFilter(field_name="st_roll", lookup_expr="startswith")
    roll_end = django_filters.CharFilter(field_name="st_roll", lookup_expr="endswith")
    
    
    class Meta:
        model = StudentModel
        fields = [
            "match_class",
            "min_class",
            "max_class",
            "match_faculty",
            "match_gender",
            "is_active",
            "match_dob",
            "admission_year",
            "admission_month",
            "recent_days",
            "old_days",
            "address_detail",
            "father_contain",
            "cont_num",
            "roll_start",
            "roll_end",
        ]