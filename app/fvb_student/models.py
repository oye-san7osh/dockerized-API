from django.db import models
from django.utils.text import slugify

# Create your models here.

class StudentModel(models.Model):
    
    class Gender(models.TextChoices):
        
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        OTHER = "O", "Other"
    
    
    st_roll = models.CharField(max_length=20, unique=True)
    st_full_name = models.CharField(max_length=75)
    st_class = models.PositiveIntegerField()
    st_faculty = models.CharField(max_length=75)
    
    
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        blank=True
    )
    
    
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    guardian_contact = models.CharField(max_length=15, blank=True)
    
    
    admission_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    
    slug = models.SlugField(unique=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(f"{self.st_full_name}-{self.st_roll}")
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.st_full_name
    
    
    
    