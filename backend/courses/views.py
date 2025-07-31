from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course, CoursePage
from .serializers import CourseSerializer, CoursePageSerializer
from .filters import CourseFilter

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all().order_by('date')
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter

class CoursePageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CoursePage.objects.all()
    serializer_class = CoursePageSerializer
