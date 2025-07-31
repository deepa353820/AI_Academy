from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CoursePageViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'pages', CoursePageViewSet, basename='coursepage')

urlpatterns = [
    path('', include(router.urls)),
]
