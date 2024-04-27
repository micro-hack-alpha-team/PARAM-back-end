"""
URL configuration for micro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path , path

from user import urls as user_urls
from fileupload import urls as upload_urls
from rest_framework.schemas import get_schema_view
from django.views.generic  import TemplateView

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(
    openapi.Info(
        title="API Schema",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

apipatterns = [
    re_path(r'^user/?', include(user_urls)),
    re_path(r'^user/?', include(upload_urls)),
    ]

urlpatterns = [
    re_path(r'^admin/?', admin.site.urls),
    re_path(r'^api/?', include(apipatterns)),
    path('api_schema/', schema_view.as_view()),
    # path('docs/', TemplateView.as_view(
    #     template_name='docs.html',
    #     extra_context={'schema_url':'api_schema'}
    #     ), name='swagger-ui'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]