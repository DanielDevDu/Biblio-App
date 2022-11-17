from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.users.api.views import Login,Logout



schema_view = get_schema_view(
   openapi.Info(
      title="Documentation API",
      default_version='v1',
      description="Biblio API Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="danieldevdu@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    # path("api/v1/", include("apps.api.urls")),
    path("api/v1/profile/", include("apps.profiles.api.routers")),
   #  path('api/v1/auth/logout/', Logout.as_view(), name = 'logout'),
   # path('api/v1/auth/login/',Login.as_view(), name = 'login'),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

# Custom views of admin site
admin.site.site_header = "BiblioApp Administration"
admin.site.site_title = "BiblioApp Admin Portal"
admin.site.index_title = "Welcome to BiblioApp Admin Portal"