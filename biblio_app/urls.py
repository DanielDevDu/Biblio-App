from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    # path('api/', include("apps.users.urls")),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('accounts/', include('django.contrib.auth.urls'))
    ]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

# Custom views of admin site
admin.site.site_header = "BiblioApp Administration"
admin.site.site_title = "BiblioApp Admin Portal"
admin.site.index_title = "Welcome to BiblioApp Admin Portal"