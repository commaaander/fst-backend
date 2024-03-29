"""fst_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from fst_backend.api import views
from fst_backend.core import views as core_views

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"group", views.GroupViewSet)
router.register(r"event", views.EventViewSet)
router.register(r"eventLocation", views.EventLocationViewSet)
router.register(r"tag", views.TagViewSet)
router.register(r"eventMedia", views.EventMediaViewSet)
router.register(r"member", views.MemberViewSet, basename="member")
router.register(r"node", views.NodeViewSet, basename="node")
router.register(r"allergies", views.AllergyViewSet)
router.register(r"person", views.PersonViewSet, basename="person")

router.register(r"siblingrelationship", views.SiblingRelationshipViewSet)
router.register(r"spouserelationship", views.SpouseRelationshipViewSet)
router.register(r"parentchildrelationship", views.ParentChildRelationshipSerializerViewSet)


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/health-check/", core_views.health_check, name="health-check"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("api/schema/v1/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/v1/", SpectacularSwaggerView.as_view(), name="api-docs"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
