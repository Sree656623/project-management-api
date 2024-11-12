from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define the Swagger schema view
schema_view = get_schema_view(
   openapi.Info(
      title="Project Management API",
      default_version='v1',
      description="API documentation for the project management tool",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@techforing.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Your app's URL where the API is implemented
    # Add the Swagger URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),  # Swagger documentation endpoint
]