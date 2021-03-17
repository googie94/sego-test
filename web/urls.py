"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.conf.urls import url
#
from rest_framework import routers
from blog.views import PostViewSet, CommentViewSet
from okr.views import TeamViewSet, UserViewSet, ObjectiveViewSet, KeyResultViewSet, OkrProgressViewSet
#
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_url_patterns = [ path('api/v1/', include('web.urls')), ]
schema_view = get_schema_view(
   openapi.Info(
      title="SEGO API",
      default_version='v1',
      description="study RESTAPI",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,), 
   patterns=schema_url_patterns,
)
router = routers.DefaultRouter()
router.register(r'blog', PostViewSet)
router.register(r'comment', CommentViewSet)
#
router.register(r'team', TeamViewSet)
router.register(r'user', UserViewSet)
router.register(r'objective', ObjectiveViewSet)
router.register(r'keyresult', KeyResultViewSet)
router.register(r'okrprogress', OkrProgressViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('polls/', include('polls.urls')),
    path('okr/', include('okr.urls')),
    #
    path('scraping/', include('scraping.urls')),
    #
    # path('snippet/', include('snippets.urls')),
    #
    path('api/v1/', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
