from django.urls import include, path

from .views import UsuarioViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
]