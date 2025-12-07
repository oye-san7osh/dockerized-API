
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT AUTHENTICATION ENDPOINTS
    path('api/token/', TokenObtainPairView.as_view(), name = "token_obtain_par"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = "token_refresh"),
    
    
    path('api/', include("fvb_student.urls")),
]
