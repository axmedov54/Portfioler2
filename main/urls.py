from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API documentation",
        terms_of_service="###",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="DATA UNION"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)